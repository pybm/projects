from django.db import models

class Notes(models.Model):
  name = models.CharField(max_length=255)
  details = models.CharField(max_length=255)
  link = models.URLField(max_length=255)
