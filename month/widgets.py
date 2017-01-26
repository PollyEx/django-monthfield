"""
Select widget for MonthField. Copied and modified from
https://docs.djangoproject.com/en/1.8/ref/forms/widgets/#base-widget-classes
"""
from datetime import date
from django.forms import widgets
from django.utils.dates import MONTHS

from month.util import string_type


class MonthSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        _widgets = (
            widgets.Select(attrs=attrs, choices=MONTHS.items()),
            # widgets.Select(attrs=attrs, choices=years),
            widgets.TextInput(attrs=attrs),
        )
        super(MonthSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            if isinstance(value, string_type):
                m = int(value[5:7])
                y = int(value[:4])
                return [m, y]
            return [value.month, value.year]
        return [None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=1, month=int(datelist[0]),
                     year=int(datelist[1]))
        except ValueError:
            return ''
        else:
            return str(D)
