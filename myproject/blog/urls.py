from django.urls import path
from .views import  ArticleDetail,CategoryList,ArticleList

app_name = 'blog'

urlpatterns = [
    path('article/<slug:slug>/', ArticleDetail.as_view(), name='detailArticle'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>',  CategoryList.as_view(), name='category'),
    path('', ArticleList.as_view(), name='ArticleList'),
    path('page/<int:page>', ArticleList.as_view(), name='ArticleList'),
] 