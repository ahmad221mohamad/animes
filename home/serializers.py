from rest_framework import serializers
from .models import Anime,Episodes
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = [
            "title", 
            "description", 
            "description_ar",
             "image",
              "category",
              "status",
              "years_of_production",
              "views_counts",
              "episode_numbers",
              "studio",
              "rating",
              "trailer",
              "slug",
              ]
class EpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = [
            "epanmname",
            "epnumber",
            "epurl",
            "epslug",
            "epdlink",
        ]