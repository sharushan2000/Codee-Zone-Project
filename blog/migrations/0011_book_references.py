# Generated by Django 5.1 on 2024-08-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_page_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='references',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
