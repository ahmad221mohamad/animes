# Generated by Django 4.0.2 on 2022-05-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_anime_slug_alter_episodes_epslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
