# coding=utf-8
import os
from PIL import Image, ImageDraw, ImageFont
from tracking.program.models import Venue, VenueAttendance

def make_font(font_size):
    return ImageFont.truetype(
        os.path.join(os.path.dirname(__file__), 'fonts/GenShinGothic-Regular.ttf'),
        font_size
    )


def generate_heatmap(f):
    audiences = {}
    for venue in Venue.objects.all():
        audiences[venue.id] = VenueAttendance.objects.filter(is_enabled=True, venue=venue).count()


    img = Image.open(os.path.join(os.path.dirname(__file__), 'files/hall.png'))

    draw = ImageDraw.Draw(img)
    draw.font = make_font(50)

    # 大きい
    draw.text((272, 170), str(audiences[1]), (255, 0, 0))

    # A
    draw.text((160, 116), str(audiences[2]), (255, 0, 0))

    # B
    draw.text((160, 180), str(audiences[3]), (255, 0, 0))

    draw.font = make_font(40)

    # C
    draw.text((370, 112), str(audiences[4]), (255, 0, 0))

    # D
    draw.text((450, 112), str(audiences[5]), (255, 0, 0))

    # E
    draw.text((520, 160), str(audiences[6]), (255, 0, 0))


    img.save(f, "PNG")
    return f
