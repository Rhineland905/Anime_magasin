from django.urls import path
from apps.user.views import user_login, user_register, user_logout

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
]