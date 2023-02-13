from django.urls import path
from apps.api.Category.views import CategoryCreatViews, CategoryDetailViews, CategoryListViews, ProductUpdateViews, \
    ProductDeleteViews

urlpatterns = [
    path('category/', CategoryListViews.as_view()),
    path('category/<int:pk>/', CategoryDetailViews.as_view()),
    path('category/creat/', CategoryCreatViews.as_view()),
    path('category/update<int:pk>/', ProductUpdateViews.as_view()),
    path('category/delete<int:pk>/', ProductDeleteViews.as_view()),

]