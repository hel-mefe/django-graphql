import graphene
from graphene_django.types import DjangoObjectType
from .models import Game

# Define a DjangoObjectType for your model
class GameType(DjangoObjectType):
    class Meta:
        model = Game

# Define a Query class that inherits from graphene.ObjectType
class GameQuery(graphene.ObjectType):
    # Define fields for your query
    all_games = graphene.List(GameType)
    
    # Define a resolver function to resolve the query
    def resolve_all_games(self, info):
        return Game.objects.all()
