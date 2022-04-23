# Generated by Django 4.0.2 on 2022-04-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_trail_anime_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='category_ar',
            field=models.ManyToManyField(blank=True, related_name='categoryar', to='home.Category'),
        ),
        migrations.AddField(
            model_name='anime',
            name='description_ar',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='category',
            field=models.ManyToManyField(blank=True, to='home.Category'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
