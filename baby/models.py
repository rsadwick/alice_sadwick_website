from django.db import models
from django import forms

class Baby(models.Model):
    week = models.SmallIntegerField()
    fruit_title = models.CharField(max_length=100)
    fruit_img = models.CharField(max_length=80)
    baby_title = models.CharField(max_length=100)
    baby_img = models.CharField(max_length=80)

class Rsvp(models.Model):
    name = models.CharField(max_length=100)
    coming = models.BooleanField()

class RsvpForm(forms.Form):
    name = forms.CharField(max_length=100)
    coming = forms.BooleanField( widget = forms.HiddenInput() )

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=12000)
    slug = models.CharField(max_length=30)

    def __unicode__(self):
        return self.slug
