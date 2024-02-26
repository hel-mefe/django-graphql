import graphene
from graphene_django.types import DjangoObjectType
from ..models import Game

class GameType(DjangoObjectType):
    class Meta:
        model = Game

