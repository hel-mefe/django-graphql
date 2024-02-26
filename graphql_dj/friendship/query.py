import graphene
from graphene_django.types import DjangoObjectType
from .models import Friendship

# Define a DjangoObjectType for your model
class FriendshipTyoe(DjangoObjectType):
    class Meta:
        model = Friendship

# Define a Query class that inherits from graphene.ObjectType
class FrinedshipQuery(graphene.ObjectType):
    # Define fields for your query
    all_friendships = graphene.List(FriendshipType)
    
    # Define a resolver function to resolve the query
    def resolve_all_friendships(self, info):
        return Friendship.objects.all()
