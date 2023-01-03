from django.views import generic
from apps.catalog.models import Category

class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/index.html'
    queryset = Category.objects.filter(parent=None)

