from django.urls import path
from apps.api.catalog.views import ProductListViews , ProductDetailViews,ProductCreatViews, ProductUpdateViews,ProductDeleteViews

urlpatterns = [
    path('product/', ProductListViews.as_view()),
    path('product/<int:pk>/', ProductDetailViews.as_view()),
    path('product/creat/', ProductCreatViews.as_view()),
    path('product/update<int:pk>/', ProductUpdateViews.as_view()),
    path('product/delete<int:pk>/', ProductDeleteViews.as_view()),

]
