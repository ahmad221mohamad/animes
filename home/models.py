from re import T
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    catname=models.CharField(max_length=50)
    catname_ar=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.catname
STATUS=(
    ('RA','RECRNTLY ADDED'),
    ('MW','MOST WATHED'),
    ('TR','TOP RATED'),
)
class Anime(models.Model):
    title=models.CharField(max_length=1000)
    description=models.TextField(max_length=1000,null=True,blank=True)
    description_ar=models.TextField(max_length=1000,null=True,blank=True)
    image=CloudinaryField('image')
    category=models.ManyToManyField(Category,blank=True)
    status=models.CharField(choices=STATUS,max_length=2)
    years_of_production=models.DateField()
    views_counts=models.IntegerField(default=0)
    episode_numbers=models.IntegerField(default=0)
    studio=models.CharField(max_length=50,null=True,blank=True)
    rating=models.FloatField(default=0)
    trailer=models.URLField(null=True,blank=True)
    slug=models.SlugField(blank=True,null=True,max_length=1000)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Anime,self).save()
    def __str__(self):
        return self.title
class Episodes(models.Model):
    epanmname=models.ForeignKey(Anime,on_delete=models.CASCADE)
    epnumber=models.IntegerField(default=0)
    epurl=models.URLField(blank=True,null=True)
    epslug=models.SlugField(blank=True,null=True,max_length=1000)
    epdlink=models.URLField(blank=True,null=True)
    epimage=CloudinaryField(blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.epslug:
            self.epslug=slugify(self.epanmname.title+'-ep-'+str(self.epnumber))
        if not self.epimage:
            self.epimage=self.epanmname.image
        super(Episodes,self).save()
        
    def __str__(self):
        return self.epslug,self.epimage