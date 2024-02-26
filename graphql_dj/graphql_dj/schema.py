from friendship.graphql.query import FriendshipQuery
from friendship.graphql.mutation import FriendshipMutation
from game.graphql.query import GameQuery
from game.graphql.mutation import GameMutation
from notification.graphql.query import NotificationQuery
from notification.graphql.mutation import NotificationMutation
from tournament.graphql.query import TournamentQuery
from tournament.graphql.mutation import TournamentMutation
from user.graphql.query import UserQuery
from user.graphql.mutation import UserMutation
import graphene
from graphene_django.types import DjangoObjectType

class Query(FriendshipQuery, GameQuery, NotificationQuery, TournamentQuery, UserQuery):
    pass

class Mutation(FriendshipMutation, GameMutation, NotificationMutation, TournamentMutation, UserMutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)