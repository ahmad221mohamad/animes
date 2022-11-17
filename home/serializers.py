from rest_framework import serializers
from .models import Anime, Category,Episodes
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = [
            "id",
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
            "id",
            "epimage",
            "epanmtitle",
        ]
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
           "catname",
           "catname_ar",
        ]