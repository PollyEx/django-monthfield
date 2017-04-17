from django.db import models
from month.models import MonthField


# Create your models here.

class Example(models.Model):
    name = models.CharField(max_length=20, blank=True)
    month = MonthField("Month Value", help_text="some help...")

    def __unicode__(self):
        return unicode(self.month)
