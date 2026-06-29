from django.contrib import admin
from .models import *


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'size',
        'created_at',
    )

    search_fields = (
        'name',
        'user__username',
    )

    list_filter = (
        'created_at',
    )


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'parent',
    )