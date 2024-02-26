import graphene
from graphene_django.types import DjangoObjectType
from ..models import Friendship

class FriendshipType(DjangoObjectType):
    class Meta:
        model = Friendship

