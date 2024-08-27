from django.utils.text import slugify
from django.dispatch import receiver
from .models import Article,Chapter
from django.db.models.signals import post_save


@receiver(post_save, sender=Article)
def create_book_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(f"{instance.title}_{instance.author}")
        instance.save()

@receiver(post_save, sender=Chapter)
def add_chapter_number(sender,instance,created,**kwargs):
 
    if created:
        instance.chapter_number = instance.article.chapters.count()
        instance.save()


