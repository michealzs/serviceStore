from django.db import models

class HomeModel(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    text = models.text()
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.title
