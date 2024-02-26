from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    player1 = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey('user.User', on_delete=models.CASCADE,  related_name='player2')
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    winner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='winner')