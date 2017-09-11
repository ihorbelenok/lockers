# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    name = models.CharField(max_length=16, verbose_name="Клас")

    def __unicode__(self):
        return self.name

class Kid(models.Model):
    name = models.CharField(max_length=254, verbose_name="ПІБ учня")
    school_class = models.ForeignKey('SchoolClass')

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.school_class.name)

class Locker(models.Model):
    number = models.CharField(unique=True, max_length=254, verbose_name="Номер шафи")
    code = models.CharField(max_length=254, verbose_name="Код")
    # owner = models.ForeignKey('Kid', blank=True, null=True, default=None)
    kid = models.CharField(max_length=254, verbose_name="Власник", blank=True)
    kid_class = models.CharField(max_length=32, verbose_name="Клас", blank=True)

    address = models.TextField(blank=True, verbose_name="Адреса")
    phone = models.CharField(max_length=32, blank=True, verbose_name="Телефон")

    def __unicode__(self):
        return "%s" % (self.number)