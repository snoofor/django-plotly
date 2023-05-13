from django.db import models

# Create your models here.

class GetFile(models.Model):
    file = models.FileField(upload_to='uploads')