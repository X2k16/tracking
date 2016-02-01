# coding=utf-8
import os
from tempfile import NamedTemporaryFile
import subprocess
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from PIL import Image
import qrcode


def _register_fonts():
    fonts = ["GenShinGothic-Regular", "GenShinGothic-Light"]

    for font in fonts:
        pdfmetrics.registerFont(TTFont(font, "{0}/fonts/{1}.ttf".format(os.path.dirname(__file__), font)))

_register_fonts()


def drawCenteredString(page, fontname, size, x, y, text):
    page.setFont(fontname, size)
    x -= (pdfmetrics.stringWidth(text, fontName=fontname, fontSize=size) / 2.0)
    page.drawString(x, y, text)


def drawLeftString(page, fontname, size, x, y, text):
    page.setFont(fontname, size)
    page.drawString(x, y, text)


def drawRightString(page, fontname, size, x, y, text):
    page.setFont(fontname, size)
    x -= pdfmetrics.stringWidth(text, fontName=fontname, fontSize=size)
    page.drawString(x, y, text)


def generate_sheet_pdf(part, f):

    # 印字内容の生成
    buffer = NamedTemporaryFile(suffix=".pdf", delete=True)
    page = canvas.Canvas(buffer, pagesize=A4)

    for i, perticipant in enumerate(part):
        page.saveState()
        part_x = i % 3
        part_y = int(i / 3)
        page.translate((7.2 + ((63.5 + 2.55) * part_x)) * mm, (15.15 + 38.1 * (6 - part_y)) * mm)

        # QRコード
        img = qrcode.make("https://ticket.cross-party.com/tracking/l/?t={0}".format(perticipant.login_token))._img
        page.drawImage(ImageReader(img), 0, (38.1 - 30) / 2 * mm, 30 * mm, 30 * mm)

        # No.0000
        drawRightString(page, "GenShinGothic-Light", 3 * mm, (63.5 - 2) * mm, 2 * mm, "No.{0:04d}".format(perticipant.id))

        # アンケート
        drawCenteredString(page, "GenShinGothic-Regular", 3.5 * mm, 45 * mm, 27.2 * mm, "アンケートに")
        drawCenteredString(page, "GenShinGothic-Regular", 3.5 * mm, 45 * mm, 23 * mm, "← 答えて")
        drawCenteredString(page, "GenShinGothic-Regular", 3.5 * mm, 45 * mm, 18.8 * mm, "景品を当てよう！")

        drawCenteredString(page, "GenShinGothic-Regular", 4 * mm, 45 * mm, 12 * mm, "リーダーに")
        drawCenteredString(page, "GenShinGothic-Regular", 4 * mm, 45 * mm, 8 * mm, "ここをタッチ♪")

        # グリッド
        page.line(0, 0, 63.5 * mm, 0)
        page.line(63.5 * mm, 0, 63.5 * mm, 38.1 * mm)
        page.line(63.5 * mm, 38.1 * mm, 0, 38.1 * mm)
        page.line(0, 38.1 * mm, 0, 0)

        page.restoreState()

    page.showPage()
    page.save()
    buffer.seek(0)

    f.write(buffer.read())

    buffer.close()
    return f


def generate_sherets_pdf(perticipants, f):
    buffers = []
    while len(perticipants.order_by("id")):
        part = perticipants[:21]
        perticipants = perticipants[21:]
        buffer = NamedTemporaryFile(suffix=".pdf", delete=True)
        generate_sheet_pdf(part, buffer)
        buffers.append(buffer)

    output = NamedTemporaryFile(suffix=".pdf", delete=True)
    cmd = ["pdftk"]
    cmd += [buffer.name for buffer in buffers]
    cmd += ["output", output.name]
    subprocess.call(cmd)

    output.seek(0)

    f.write(output.read())
    output.close()
    for buffer in buffers:
        buffer.close()

    return f
