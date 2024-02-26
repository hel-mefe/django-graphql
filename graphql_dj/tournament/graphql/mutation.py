import graphene
from graphene_django.types import DjangoObjectType
from .type import TournamentType
from ..models import Tournament

class TournamentMutation(graphene.ObjectType):
    pass