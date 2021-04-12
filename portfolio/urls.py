from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('detail/<pk>/',views.DetailView.as_view(), name='detail')
]
