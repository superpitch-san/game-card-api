# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Score(models.Model):
    top_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return '%s %s' % (self.score_id, self.top_score)
