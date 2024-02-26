import graphene
from graphene_django.types import DjangoObjectType
from .models import UserSettings

# Define a DjangoObjectType for your model
class UserSettingsType(DjangoObjectType):
    class Meta:
        model = UserSettings

# Define a Query class that inherits from graphene.ObjectType
class UserSettingsQuery(graphene.ObjectType):
    # Define fields for your query
    all_users_settings = graphene.List(UserSettings)
    
    # Define a resolver function to resolve the query
    def resolve_all_users_settings(self, info):
        return UserSettings.objects.all()
