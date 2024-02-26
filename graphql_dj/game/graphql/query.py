import graphene
from graphene_django.types import DjangoObjectType
from ..models import Game
from .type import GameType

class GameQuery(graphene.ObjectType):
    pass

## DEMO CODE:
    # chess = graphene.String()
    # done = graphene.String()

    # def resolve_chess(parent, info):
    #     return 'CHESS!'
    
    # def resolve_done(parent, info):
    #     print('****** PARENT *******')
    #     print(parent)
    #     print('***** INFO *********')
    #     print(info)
    #     return 'DONE!!'