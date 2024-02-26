import graphene
from graphene_django.types import DjangoObjectType
from ..models import Notification
from .type import NotificationType

class NotificationQuery(graphene.ObjectType):
    pass