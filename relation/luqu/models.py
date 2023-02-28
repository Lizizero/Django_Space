from django.db import models


# Create your models here.
class zyxx(models.Model):
    zsdm = models.CharField(max_length=8)
    zymc = models.CharField(max_length=8)
    level = models.CharField(max_length=8)
    charge = models.CharField(max_length=8)

    def __str__(self):
        return "%s %s %s %s" % (self.zsdm, self.zymc, self.level, self.charge)


class lqxx(models.Model):
    zkzh = models.CharField(max_length=10)
    name = models.CharField(max_length=8)
    lqzy = models.ForeignKey(zyxx, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s %s" % (self.zkzh, self.name, self.lqzy.zsdm)
