from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Project

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['portfolio']

    def location(self, item):
        return reverse(item)

class DetailSitemap(Sitemap):

    def items(self):
        return Project.objects.all()