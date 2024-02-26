import graphene
from graphene_django.types import DjangoObjectType
from ..models import UserSettings
from .type import UserSettingsType

class UserSettingsQuery(graphene.ObjectType):
    pass