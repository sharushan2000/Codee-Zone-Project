from django.db import models

from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type


class Article(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200,blank=True,null=True)
    book_cover = models.ImageField(upload_to='book_cover/',blank=True,null=True)
    author = models.CharField(max_length=100)
    category = models.ManyToManyField(Category,related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    github_link = models.URLField(blank=True,null=True)
    references = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    title = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='chapters')
    chapter_number = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='coding_images/', blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_next_page = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.article.title} - Chapter {self.chapter_number}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}_{self.chapter_number}_{self.article.title}")
        super().save(*args, **kwargs)
