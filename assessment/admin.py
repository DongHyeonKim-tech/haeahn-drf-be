from django.contrib import admin
from assessment.models import TbBimCertificationManager, TbBimCertificationTest, TbBimCertificationTestUser, TbBimCertificationTestUserQuestion

# Register your models here.
# admin site에 model 추가

class manager_model(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'dept_cd', 'dept_name', 'is_executive', 'is_used', 'description', 'is_bim_team']

class test_model(admin.ModelAdmin):
    list_display = ('name','test_type', 'test_datetime', 'max_participants', 'registration_start_date', 'registration_end_date', 'is_opened', 'is_generated_question', 'result_open_on', 'is_result_open')
    search_fields = ['name']
    
class test_user_model(admin.ModelAdmin):
    list_display = ['test_id', 'user_id', 'registration_datetime', 'start_datetime', 'end_datetime', 'is_submitted', 'submitted_on', 'is_observer', 'is_canceled', 'is_exception']

class test_user_question_model(admin.ModelAdmin):
    list_display = ['test_id', 'user_id', 'question_id', 'category', 'content', 'question_group'] 

admin.site.register(TbBimCertificationManager, manager_model)
admin.site.register(TbBimCertificationTest, test_model)
admin.site.register(TbBimCertificationTestUser, test_user_model)
admin.site.register(TbBimCertificationTestUserQuestion, test_user_question_model)
