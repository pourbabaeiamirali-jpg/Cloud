from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import FileUploadForm
from .models import File


class FileListView(
    LoginRequiredMixin,
    ListView
):
    model = File
    template_name = 'files/file_list.html'
    paginate_by = 20

    def get_queryset(self):
        qs = File.objects.filter(
            user=self.request.user
        )

        search = self.request.GET.get('q')

        if search:
            qs = qs.filter(
                name__icontains=search
            )

        return qs


class FileUploadView(
    LoginRequiredMixin,
    CreateView
):
    model = File
    form_class = FileUploadForm
    template_name = 'files/upload.html'
    success_url = reverse_lazy(
        'files:list'
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FileDeleteView(
    LoginRequiredMixin,
    DeleteView
):
    model = File
    success_url = reverse_lazy(
        'files:list'
    )

    def get_queryset(self):
        return File.objects.filter(
            user=self.request.user
        )


class FileDownloadView(
    LoginRequiredMixin,
    View
):
    def get(self, request, pk):
        file_obj = get_object_or_404(
            File,
            pk=pk,
            user=request.user
        )

        return FileResponse(
            file_obj.file.open('rb'),
            as_attachment=True,
            filename=file_obj.name
        )