import graphene
from graphene_django.types import DjangoObjectType
from .models import Notification

# Define a DjangoObjectType for your model
class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification

# Define a Query class that inherits from graphene.ObjectType
class NotificationQuery(graphene.ObjectType):
    # Define fields for your query
    all_notifications = graphene.List(NotificationType)
    
    # Define a resolver function to resolve the query
    def resolve_all_notifications(self, info):
        return Notification.objects.all()
