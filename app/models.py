from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"