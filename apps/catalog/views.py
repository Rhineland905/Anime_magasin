from django.urls import reverse
from django.views import generic
from apps.catalog.models import Category, Product


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/index.html'
    queryset = Category.objects.filter(parent=None)


class ProductsByCategoryView(generic.ListView):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(categories=self.category)
        return queryset

    def set_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): "Каталог"}

        category = self.category
        categories = []
        parent = category.parent
        while parent is not None:
            categories.append((reverse('categories', args=[parent.slug]), parent.name))
            parent = parent.parent
        for key, value in categories[::-1]:
            breadcrumbs.update({key: value})

        breadcrumbs.update({'current': self.category.name})
        return breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        context['breadcrumbs'] = self.set_breadcrumbs()
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def set_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): "Каталог"}

        category = self.object.main_category()
        if category:
            categories = [(reverse('categories', args=[category.slug]), category.name)]
            parent = category.parent
            while parent is not None:
                categories.append((reverse('categories', args=[parent.slug]), parent.name))
                parent = parent.parent
            for key, value in categories[::-1]:
                breadcrumbs.update({key: value})

        breadcrumbs.update({'current': self.object.name})
        return breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'breadcrumbs': self.set_breadcrumbs()})
        return context
