from django.db import models


class Score(models.Model):
    name = models.CharField(max_length=8)
    python = models.IntegerField()
    json = models.IntegerField()