# Generated by Django 5.1 on 2024-08-24 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_book_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter_number',
            new_name='page_number',
        ),
    ]
