# Generated by Django 5.1 on 2024-08-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
