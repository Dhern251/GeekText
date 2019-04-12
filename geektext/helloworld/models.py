from django.conf import settings
from django.db import models
from django.utils import timezone


class BookDetails(models.Model):
    author = models.CharField(max_length=200)
    authorbio = models.CharField(max_length=200)
    authorhyperlink = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    publisherinfo = models.CharField(max_length=200)
    coverphotourl = models.CharField(max_length = 1000, default = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/No_Cover.jpg')
    price = models.DecimalField(max_digits=6, decimal_places=2,default = 9.99)

    def __unicode__(self):
        return unicode(self.pk)
    
    