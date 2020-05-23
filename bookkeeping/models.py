from django.db import models

from pygments.styles import get_all_styles

STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Welcome(models.Model):
    fromIP = models.CharField(max_length=15, default='0.0.0.0')
    time = models.DateTimeField(auto_now_add=True)
    word = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['time']