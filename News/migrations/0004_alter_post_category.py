# Generated by Django 4.2.11 on 2024-04-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_rename_comment_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', through='News.PostCategory', to='News.category'),
        ),
    ]
