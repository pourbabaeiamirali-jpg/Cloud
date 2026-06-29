from django.contrib import admin
from .models import *
from .views import FileDetail


class FileAdmin(admin.ModelAdmin):
    list_display = ('name','file_type')
    list_filter = ('file_type',)
    search_fields = ('name',)
    list_per_page = 10
    list_editable = ('name',)

admin.site.register(File, FileAdmin)

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name','file_type')
    list_filter = ('file_type',)
    search_fields = ('name',)
    list_per_page = 10
    list_editable = ('name',)

admin.site.register(Folder, FolderAdmin)