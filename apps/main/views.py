from django.views import generic
from django.shortcuts import render

from apps.main.models import Page


# Create your views here.
class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()
def index(request):
    return render(request,'index.html')