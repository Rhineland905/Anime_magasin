from django.urls import path
from apps.api.user.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]