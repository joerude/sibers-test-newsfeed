# Generated by Django 4.0.5 on 2022-06-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0004_alter_news_content_alter_news_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
