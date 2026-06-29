from django.shortcuts import render
from django.views.generic import *
from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class FolderListView(ListView):
    model = Folder
    template_name = 'folder_list.html'
    context_object_name = 'folder_list'

class FolderDetailView(DetailView):
    model = Folder
    template_name = 'folder_detail.html'
    context_object_name = 'folder'

class FolderCreateView(CreateView):
    model = Folder
    template_name = 'folder_create.html'
    context_object_name = 'folder'

class FolderUpdateView(UpdateView):
    model = Folder
    template_name = 'folder_update.html'
    context_object_name = 'folder'

class FolderDeleteView(DeleteView):
    model = Folder
    template_name = 'folder_delete.html'
    context_object_name = 'folder'

class FileListView(ListView):
    model = File
    template_name = 'file_list.html'
    context_object_name = 'file_list'

class FileDetailView(DetailView):
    model = File
    template_name = 'file_detail.html'
    context_object_name = 'file'

class FileCreateView(CreateView):
    model = File
    template_name = 'file_create.html'
    context_object_name = 'file'

class FileUpdateView(UpdateView):
    model = File
    template_name = 'file_update.html'
    context_object_name = 'file'

class FileDeleteView(DeleteView):
    model = File
    template_name = 'file_delete.html'
    context_object_name = 'file'




