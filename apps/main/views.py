from django.views import generic
from django.shortcuts import render
from apps.main.models import Page,ProductSet


# Create your views here.
class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    def set_breadcrumbs(self):
        breadcrumbs = {}
        breadcrumbs.update({'current': Page.name})
        return breadcrumbs
    queryset = Page.objects.all()



def index(request):
    page = Page.objects.get(slug='home')
    product_sets = ProductSet.objects.filter(si_active=True)
    return render(request,'index.html',{'page':page,'product_sets':product_sets})