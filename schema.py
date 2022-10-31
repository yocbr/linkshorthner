import graphene

import shortener.schema
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

class Query(shortener.schema.Query, graphene.ObjectType):
    pass

class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

dark = true 
