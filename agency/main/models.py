from django.db import models

class HomeModel(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='templates/assets/images/')

    def __str__(self):
        return self.title

class AboutModel(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='templates/assets/images/')

    def __str__(self):
        return self.title
