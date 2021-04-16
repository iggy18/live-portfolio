from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Project(models.Model):
    screenshot = models.ImageField(blank=True)
    language = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    long_description = RichTextUploadingField(blank=True, null=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    video_demo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/detail/{self.pk}'

