import graphene
from graphene_django.types import DjangoObjectType
from .models import Tournament

# Define a DjangoObjectType for your model
class TournamentType(DjangoObjectType):
    class Meta:
        model = Tournament

# Define a Query class that inherits from graphene.ObjectType
class TournamentQuery(graphene.ObjectType):
    # Define fields for your query
    all_friendships = graphene.List(TournamentType)
    
    # Define a resolver function to resolve the query
    def resolve_all_friendships(self, info):
        return Tournament.objects.all()
