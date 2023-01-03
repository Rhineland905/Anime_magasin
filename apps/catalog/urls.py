from django.urls import path
from apps.catalog.views import CategoryIndexView

urlpatterns = [
    path('',CategoryIndexView.as_view(),name='catalog'),
    path('<str:slug>/',CategoryIndexView.as_view(),name='categories'),
]