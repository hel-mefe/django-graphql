import graphene
from graphene_django.types import DjangoObjectType
from .models import FriendShip


class FriendShipMutation(graphene.ObjectType):
    pass