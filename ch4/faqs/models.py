from django.db import models


# Create your models here.
class faqsdata(models.Model):
    name = models.CharField(max_length=40)
    sex = models.CharField(max_length=2, blank=True)
    age = models.IntegerField()


class scores(models.Model):
    kh = models.CharField(max_length=8)
    xm = models.CharField(max_length=8)
    yw = models.SmallIntegerField()
    sx = models.SmallIntegerField()
    bj = models.CharField(max_length=8)
