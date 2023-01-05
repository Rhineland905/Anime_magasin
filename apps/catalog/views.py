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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product.html'