from django.urls import path, include, re_path

from assessment.views import test_list_view

app_name = 'assessment'


urlpatterns = [
    path('test-list', test_list_view),
]