from django.urls import path, include, re_path

from assessment.views import test_list_view, upload_file_view, subject_list_view

app_name = 'assessment'


urlpatterns = [
    path('test-list', test_list_view),
    path('subject-list', subject_list_view),
    path('upload-file', upload_file_view)
]