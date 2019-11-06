import datetime

from django.db import models
from django.utils import timezone
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class TableAll(models.Model):
    table_name = models.CharField(max_length=250)

class UserDetail(models.Model):
    division = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    cell = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

