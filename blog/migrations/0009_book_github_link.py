# Generated by Django 5.1 on 2024-08-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_page_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
