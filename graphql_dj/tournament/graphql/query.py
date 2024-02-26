import graphene
from graphene_django.types import DjangoObjectType
from ..models import Tournament
from .type import TournamentType

class TournamentQuery(graphene.ObjectType):
    pass