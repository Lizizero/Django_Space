from django.db import models


# Create your models here.
class faqsdata(models.Model):
    question = models.CharField(max_length=200, blank=True)
    answer = models.CharField(max_length=200, blank=True)


class faqsdata2(models.Model):
    question = models.CharField(max_length=200, blank=True)
    answer = models.CharField(max_length=200, blank=True)


class faqsdata3(models.Model):
    question = models.CharField(max_length=200, blank=True)
    answer = models.CharField(max_length=200, blank=True)


class information(models.Model):
    name = models.CharField(max_length=40)
    sex = models.CharField(max_length=4)
    age = models.IntegerField()
