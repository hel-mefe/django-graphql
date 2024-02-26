import graphene
from graphene_django.types import DjangoObjectType
from .type import NotificationType
from ..models import Notification

class NotificationMutation(graphene.ObjectType):
    pass