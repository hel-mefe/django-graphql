from .query import FriendshipQuery
from .mutation import FriendshipMutation
import graphene

## Docuemntation:
#### - GraphQL Schema File
#### - Purpose: Defines the GraphQL schema
####            that the app have, this schema
####            is a sub-schema for a larger schema used inside
####            the project's folder
####
#### - Description:
####     - The friendship schema is a GraphQL schema
####       that takes 2 arguments for the moment, query and mutation
####     - query: FriendShipQuery is passed to this argument, it's mothing
####       but a class that provides some immutable functions that we can use to fetch data
####     - mutations: FriendShipMutation is passed to this argument, it's nothing
####       but a class that provides some mutable functions that we can use to set data
####
####    - Difference between Query and Mutation is that Mutation can change data inside our db
####    meanwhile Query cannot, just a way to retrieve data.
####
#### - last_edited: hel-mefe

schema = graphene.Schema(query=FriendshipQuery, mutation=FriendshipMutation)