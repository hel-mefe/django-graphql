import TournamentQuery from .query
import TournamentMutation from .mutation
import graphene

## Docuemntation:
#### - GraphQL Schema File
#### - Purpose: Defines the GraphQL schema
####            that the app have, this schema
####            is a sub-schema for a larger schema used inside
####            the project's folder
####
####
#### - last_edited: hel-mefe

schema = graphene.Schema(query=TournamentQuery, mutation=TournamentMutation)