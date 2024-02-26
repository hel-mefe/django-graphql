import graphene
from graphene_django.types import DjangoObjectType
from .type import UserSettingsType
from ..models import UserSettings

class UserSettingsMutation(graphene.ObjectType):
    pass

