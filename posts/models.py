from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    bookCover = models.FileField()
    # bookCover = models.ImageField(upload_to='static/bookCover', blank=True)
    author = models.CharField(max_length=250)
    authorbio = models.TextField()
    description = models.TextField()
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    bookrating = models.CharField(max_length=10)
    releasedate = models.CharField(max_length=50)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


