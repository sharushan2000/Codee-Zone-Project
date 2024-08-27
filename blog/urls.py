from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('',views.index,name='index'),
    path('chapter/<str:title>/<int:chapter_no>/',views.chapter_view,name='chapter_view'),
    # path('book/<str:book_title>/<int:page_number>/',views.page,name='chapter'),
    path('category/<str:category>/',views.category,name='category'),
    path('about_us/',views.about_us,name='about_us'),
]
