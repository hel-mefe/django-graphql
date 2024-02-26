import graphene
from graphene_django.types import DjangoObjectType
from .models import Friendship


class FriendshipMutation(graphene.ObjectType):
    pass