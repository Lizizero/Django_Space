from django.db import models


# Create your models here.
class banj(models.Model):
    mc = models.CharField(max_length=8)

    def __str__(self):
        return self.mc


class xues(models.Model):
    xm = models.CharField(max_length=8)
    bj = models.ForeignKey(banj, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.xm, self.bj.mc)
