from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=200)

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
