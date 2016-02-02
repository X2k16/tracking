# encoding=utf-8

from django import forms


class BootstrapMixins(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                pass
            else:
                field.widget.attrs["class"] = "form-control"
