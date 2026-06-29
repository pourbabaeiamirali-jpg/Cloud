from django.conf import settings
from django.db import models
from django.utils.text import slugify
import os
import uuid


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'user_{instance.user.id}/files/{filename}'


class Folder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='folders'
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = ('user', 'parent', 'name')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class File(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='files'
    )

    folder = models.ForeignKey(
        Folder,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='files'
    )

    name = models.CharField(max_length=255)

    file = models.FileField(
        upload_to=user_directory_path
    )

    size = models.BigIntegerField(default=0)

    mime_type = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['name']),
        ]

    def save(self, *args, **kwargs):
        if self.file:
            self.size = self.file.size

            ext = os.path.splitext(
                self.file.name
            )[1].lower()

            self.mime_type = ext

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name