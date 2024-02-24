from django.db import models
from user.models import User



class Game(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user1 = models.ForeignKey(User)
    user2 = models.ForeignKey(User)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    winner = models.ForeignKey(User)