from django.urls import path
from apps.user.views import login


urlpatterns = [
    path('user_login/', login, name='user_login'),
]
