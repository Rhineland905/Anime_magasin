from django.shortcuts import render
from django.urls import reverse
from apps.blog.forms import CreatCommets
from apps.blog.models import BlogCategory, Article, Tag, BlogComets


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {
        'current': 'Категории'

    }

    return render(request, 'blog/category_list.html', {"categories": blog_categories,"breadcrumbs":breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Категории',
        'current': category.name
    }
    return render(
        request,
        'blog/article_list.html',{'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    commets = BlogComets.objects.filter(article=article_id,is_checked=True)
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Категории', reverse('blog_article_list', args=[category_id]): category.name,
        'current': article.name
    }
    return render(request, 'blog/article_view.html', {"category": category, "article": article,"breadcrumbs":breadcrumbs,'commets':commets})


def tag_search(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    breadcrumbs = {
        'current': tag.name
    }
    return render(request, 'blog/teg_view.html', {'tag': tag, 'articles': articles,'breadcrumbs':breadcrumbs})


def commets_creat(request,article_id):
    error = None
    data = request.GET.copy()
    if request.user.is_authenticated:
        data.update(is_checked=True, name=request.user.first_name, e_mail= request.user.email, article=article_id)

    else:
        data.update(article=article_id)
    request.GET = data
    form = CreatCommets(request.GET)
    if form.is_valid():
        form.save()
        breadcrumbs = {
            'current': 'Коментарий успешно создан'
        }
        return render(request,"blog/commets_created.html",{'breadcrumbs':breadcrumbs})
    elif request.user.is_authenticated:
        error = "Скорей всего не все данные профиля не заполнини либо вы они заполнины не коректно"
    else:
        error = "Не правлино заполниная форма"

    breadcrumbs = {
        'current': 'Создания коментраия'
    }
    return render(request, 'blog/commets_creat.html',{'breadcrumbs':breadcrumbs,'blogcomets':BlogComets,'error': error,})