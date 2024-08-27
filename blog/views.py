from django.shortcuts import render,HttpResponse
from .models import Article,Chapter,Category
from django.shortcuts import  get_object_or_404
import markdown2

# Create your views here.
def index(request):
    articles = Article.objects.all()
    chapter_number = 1
    return render(request,'html/index.html',{'articles':articles
                                             ,'chapter_number':chapter_number})


"""
def article_view(request,title):
    article = Article.objects.get(title=title)
    chapters = article.chapters.all().order_by('chapter_number').order_by('chapter_number')
    first_chapter = chapters.first()
    return render(request,'html/book.html',{'article':article,'chapters':chapters,'first_chapter':first_chapter})


"""

def chapter_view(request,title,chapter_no):
    article = Article.objects.get(title=title)
    all_chapters = article.chapters.all().order_by('chapter_number')
    current_chapter = get_object_or_404(Chapter,article=article,chapter_number=chapter_no)
    markdown_content = markdown2.markdown(current_chapter.content, extras=["fenced-code-blocks"])
    next_chapter = None
    previous_chapter = None
    if chapter_no > 1:
        previous_chapter = current_chapter.chapter_number - 1
    if current_chapter.is_next_page:
        next_chapter = current_chapter.chapter_number + 1

    context = {
        'article':article,
        'current_chapter':current_chapter,
        'all_chapters':all_chapters,
        'markdown_content':markdown_content,
        'next_chapter':next_chapter,
        'previous_chapter':previous_chapter
    }
    return render(request,'html/chapter.html',context)

def category(request,category):
    category = Category.objects.get(type=category)
    article = Article.objects.filter(category=category)
    chapter_number = 1
    context ={
        'category':category,
        'articles':article,
        'chapter_number':chapter_number,
        }
    return render(request,'html/index.html',context)


def about_us(request):
    return render(request,'html/about_us.html')