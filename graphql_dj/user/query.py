import graphene
from graphene_django.types import DjangoObjectType
from .models import User

# Define a DjangoObjectType for your model
class UserType(DjangoObjectType):
    class Meta:
        model = User

# Define a Query class that inherits from graphene.ObjectType
class UserQuery(graphene.ObjectType):
    # Define fields for your query
    all_users = graphene.List(UserType)
    
    # Define a resolver function to resolve the query
    def resolve_all_users(self, info):
        return User.objects.all()
