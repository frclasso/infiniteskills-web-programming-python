from django.db import models


class Films(models.Model): #run ./manage.py sql films
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title + "," + self.year + "," + self.director