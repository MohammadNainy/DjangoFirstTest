from django.views.generic import ListView , DetailView
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404 # type: ignore
from .models import Article, Category

# Create your views here.


class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3


class ArticleDetail (DetailView) :
    def get_object (self) :
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)

def category(request,slug,page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list , 2)
    page_obj = paginator.get_page(page) 
    context = {
        'category': category,
        'articles': page_obj
    }
    return render(request, 'blog/category.html',context)
