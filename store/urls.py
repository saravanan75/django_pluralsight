from django.urls import path, re_path, include

from . import views
from .feeds import NewInventoryFeed
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from .sitemaps import LatestSitemap

sitemaps = {
    'latest': LatestSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('feed', NewInventoryFeed()),
    path('newitem', views.newitem, name='newitem'),
    re_path(r'^\d+', views.detail, name='detail'),
    re_path(r'^electronics', views.electronics, name='electronics'),
    re_path(r'^logout', views.logout, name='logout'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap')

]


