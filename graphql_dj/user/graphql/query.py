import graphene
from graphene_django.types import DjangoObjectType
from ..models import User
from .type import UserType

class UserQuery(graphene.ObjectType):
    pass