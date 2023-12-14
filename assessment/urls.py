from django.urls import path, include, re_path

from assessment.views import mssql_view

app_name = 'assessment'


urlpatterns = [

    path('mssql_view', mssql_view),
]