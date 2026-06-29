from django.urls import path
from .views import *

app_name = 'files'

urlpatterns = [
    path(
        '',
        FileListView.as_view(),
        name='list'
    ),

    path(
        'upload/',
        FileUploadView.as_view(),
        name='upload'
    ),

    path(
        '<int:pk>/download/',
        FileDownloadView.as_view(),
        name='download'
    ),

    path(
        '<int:pk>/delete/',
        FileDeleteView.as_view(),
        name='delete'
    ),
]