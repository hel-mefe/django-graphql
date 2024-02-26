import graphene
from graphene_django.types import DjangoObjectType
from .models import User


class UserMutation(graphene.ObjectType):
    pass