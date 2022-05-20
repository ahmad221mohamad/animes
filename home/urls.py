from home.sitemap import AnimeSitemap, EpisodesSitemap
from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
sitemaps = {
    'watching':EpisodesSitemap,
    '':AnimeSitemap
}
urlpatterns = [
   path('',views.home,name='home'),
   path('json',views.jsondata),
   path('json/ep',views.jsondataep),
   path("watching/<str:epslug>",views.watching,name='watching'),
   path('search-resulte',views.search,name='search'),
   path('categories-<str:categories>',views.categories,name='categories'),
   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]