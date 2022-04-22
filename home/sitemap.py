from . models import Anime,Episodes
from django.contrib.sitemaps import Sitemap
 
class AnimeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Anime.objects.all()

        
    def location(self,obj):
        return '/%s' % (obj.slug)
 
class EpisodesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Episodes.objects.all()

        
    def location(self,obj):
        return '/watching/%s' % (obj.epslug)