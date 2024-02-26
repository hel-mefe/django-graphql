import graphene
from graphene_django.types import DjangoObjectType
from .type import UserType
from ..models import User

class UserMutation(graphene.ObjectType):
    pass