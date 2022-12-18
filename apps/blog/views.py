from django.shortcuts import render
from apps.blog.models import BlogCategory, Article,Tag

# Create your views here.
def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category_list.html', {"categories": blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article_list.html', {'articles': articles, "category": category})


def article_viwe(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article_view.html', {'article': article, "category": category})

def teg_shear(request, teg_id):
    teg_id = Tag.objects.get(id=teg_id)
    article = Article.objects.filter(tags =teg_id)

    return render(request,'blog/teg_view.html',{'teg_id':teg_id,'article':article})