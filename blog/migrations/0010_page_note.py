# Generated by Django 5.1 on 2024-08-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_book_github_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
