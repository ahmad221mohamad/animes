# Generated by Django 4.0.2 on 2022-04-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_anime_category_ar_anime_description_ar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='category_ar',
        ),
        migrations.AddField(
            model_name='category',
            name='catname_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]