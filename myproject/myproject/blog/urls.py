from django.urls import path
from .views import  ArticleDetail,category,ArticleList

app_name = 'blog'

urlpatterns = [
    path('article/<slug:slug>/', ArticleDetail.as_view(), name='detailArticle'),
    path('category/<slug:slug>/', category, name='category'),
    path('category/<slug:slug>/page/<int:page>', category, name='category'),
    path('', ArticleList.as_view(), name='ArticleList'),
    path('page/<int:page>', ArticleList.as_view(), name='ArticleList'),
] 