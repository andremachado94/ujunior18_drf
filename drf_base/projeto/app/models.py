# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Sport(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('name',)


class Player(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    age = models.IntegerField(blank=True, default=-1)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

# Create your models here.
