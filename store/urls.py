from django.urls import path, re_path

from . import views
from .views import ElectronicsView3

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^\d+', views.detail, name='detail'),
    re_path(r'^electronics', views.electronics, name='electronics'),
    re_path(r'^logout', views.logout, name='logout'),
    #re_path(r'^electronics', ElectronicsView3.as_view(), name='electronics'),

]

