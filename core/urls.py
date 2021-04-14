from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap, DetailSitemap

sitemaps = {
    'static' : StaticViewSitemap,
    'project' : DetailSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
