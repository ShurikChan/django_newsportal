# Generated by Django 4.2.11 on 2024-07-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_categorysubs_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
