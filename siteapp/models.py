from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=50)
    iframe = models.CharField(max_length=1000)
    date = models.DateTimeField('date')

    def __unicode__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=300)
    youtube_link = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title

class photoAlbum(models.Model):
    title = models.CharField(max_length=300)

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=300)
    src = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    album = models.ForeignKey(photoAlbum, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class contactResponse(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    favorite_color = models.CharField(max_length=10)
    hero = models.CharField(max_length=300)
    simpsons = models.CharField(max_length=600)
    book = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.name