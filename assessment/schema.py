import graphene
from graphene_django.types import DjangoObjectType

from .models import TbBimCertificationManager
from graphql import GraphQLError

class ManagerType(DjangoObjectType):
    class Meta:
        model = TbBimCertificationManager
        
class Query(object):
    manager = graphene.Field(ManagerType, user_id = graphene.String())
    
    def resolve_manager(self, info, **kwargs):
        # user_id = kwargs.get('user_id')
        # return TbBimCertificationManager.objects.filter(user_id=user_id).first()
        
        return TbBimCertificationManager.objects.all().values()
                