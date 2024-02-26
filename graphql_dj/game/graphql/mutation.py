import graphene
from graphene_django.types import DjangoObjectType
from .type import GameType
from ..models import Game

class GameMutation(graphene.ObjectType):
    pass