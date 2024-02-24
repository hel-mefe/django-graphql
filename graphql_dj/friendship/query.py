import graphene
from graphene_django.types import DjangoObjectType
from .models import FriendShip

# Define a DjangoObjectType for your model
class FriendShipType(DjangoObjectType):
    class Meta:
        model = FriendShip

# Define a Query class that inherits from graphene.ObjectType
class FriendShipQuery(graphene.ObjectType):
    # Define fields for your query
    all_friendships = graphene.List(FriendShipType)
    
    # Define a resolver function to resolve the query
    def resolve_all_friendships(self, info):
        return FriendShip.objects.all()
