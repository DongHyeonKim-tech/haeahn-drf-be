import graphene

from assessment.schema import Query as ManagerQuery

class Query(ManagerQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

