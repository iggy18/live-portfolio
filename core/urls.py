from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap, DetailSitemap
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'static' : StaticViewSitemap,
    'project' : DetailSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^robots\.txt', include('robots.urls')),
]

handler404 = 'portfolio.views.error_404_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
