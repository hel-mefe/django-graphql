import graphene
from graphene_django.types import DjangoObjectType
from ..models import UserSettings

class UserSettingsType(DjangoObjectType):
    class Meta:
        model = UserSettings

