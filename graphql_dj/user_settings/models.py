from django.db import models

# Create your models here.
class UserSettings(models.Model):
    id = models.AutoField(primary_key=True)