from django.db import models


class score(models.Model):
    name = models.CharField(max_length=8)
    python = models.IntegerField()
    js = models.IntegerField()
