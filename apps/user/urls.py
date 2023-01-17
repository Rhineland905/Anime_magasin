from django.urls import path
from apps.user.views import user_login


urlpatterns = [
    path('login/', user_login, name='login'),
]