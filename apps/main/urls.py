from django.urls import path
from apps.main.views import PageView, index

urlpatterns = [
    path('',index, name='index'),
    path('<str:slug>/',PageView.as_view(), name='page')
]