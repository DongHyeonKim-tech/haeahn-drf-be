from django.contrib import admin
from assessment.models import TbBimCertificationComm, TbBimCertificationManager, TbBimCertificationTest

# Register your models here.
# admin site에 model 추가
admin.site.register(TbBimCertificationComm)
admin.site.register(TbBimCertificationManager)
admin.site.register(TbBimCertificationTest)