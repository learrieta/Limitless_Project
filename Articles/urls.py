from django.urls import path
from Articles import views

urlpatterns = [
    path('', views.article_list, name="home_page"),
]