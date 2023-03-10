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
   path('api',views.AnimeListApiView.as_view()),
   path('api/search/',views.Anime_SearchListApiView.as_view()),
   path('api/anime/',views.Anime_imgListApiView.as_view()),
   path('api/ep/',views.AnimeoDetailApiView.as_view()),
   path('api/ep_list/',views.EpsApiView.as_view()),
   path('api/categories_list/',views.Catgories_ListApiView.as_view()),
   path('api/cat/',views.CatDetailApiView.as_view()),
   path("watching/<str:epslug>",views.watching,name='watching'),
   path('search-resulte',views.search,name='search'),
   path('categories-<str:categories>',views.categories,name='categories'),
   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]