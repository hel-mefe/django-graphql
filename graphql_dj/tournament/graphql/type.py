import graphene
from graphene_django.types import DjangoObjectType
from ..models import Tournament

class TournamentType(DjangoObjectType):
    class Meta:
        model = Tournament