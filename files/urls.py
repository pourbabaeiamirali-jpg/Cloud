from django.urls import path
from .views import *

urlpatterns = [
    path('', FolderListView.as_view(), name='folder_list'),
    path('<int:pk>/', FolderDetailView.as_view(), name='folder_detail'),
    path('<int:pk>/delete/', FolderDeleteView.as_view(), name='folder_delete'),
    path('create/', FolderCreateView.as_view(), name='folder_create'),
    path('<int:pk>/update/', FolderUpdateView.as_view(), name='folder_update'),
]