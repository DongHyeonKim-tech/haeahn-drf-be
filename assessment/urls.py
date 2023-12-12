from django.urls import path, include, re_path

from assessment.views import mongoclient_view, djongo_view, mssql_view

app_name = 'assessment'


urlpatterns = [

    path('mongoclient_view', mongoclient_view),
    path('djongo_view', djongo_view),
    path('mssql_view', mssql_view),
]