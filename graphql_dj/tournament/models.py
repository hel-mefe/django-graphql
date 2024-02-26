from django.db import models
from enumfields import Enum, EnumField

#### Documentation:
##
##
##
##

class TournamentState(Enum):
    ONGOING = 'ONGOING'
    WAITING = 'WAITING'
    FINISHED = 'FINISHED'

# Create your models here.
class Tournament(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    state = EnumField(TournamentState, default=TournamentState.WAITING)