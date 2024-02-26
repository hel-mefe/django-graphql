from django.db import models
from friendship.models import Friendship
from user_settings.models import UserSettings
from game.models import Game
from tournament.models import Tournament

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=False)
    friends = models.ManyToManyField(Friendship)
    settings = models.ForeignKey(UserSettings, on_delete=models.CASCADE, related_name='settings')
    games = models.ManyToManyField(Game)
    tournaments = models.ManyToManyField(Tournament)