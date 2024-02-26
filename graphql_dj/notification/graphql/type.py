import graphene
from graphene_django.types import DjangoObjectType
from ..models import Notification

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification

