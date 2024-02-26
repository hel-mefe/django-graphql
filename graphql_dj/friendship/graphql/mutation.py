import graphene
from graphene_django.types import DjangoObjectType
from .type import FriendshipType
from ..models import Friendship

class CreateFriendship(graphene.Mutation):
    class Arguments:
        pass

    friendship = graphene.Field(FriendshipType)

    def mutate(self, info, **kwargs):
        # Your mutation logic to create friendship
        return CreateFriendship(friendship=friendship)

class FriendshipMutation(graphene.ObjectType):
    create_friendship = CreateFriendship.Field()