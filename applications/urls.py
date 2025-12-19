from django.urls import path

from .views import ApplicationCreateView

urlpatterns = [
    path('apply/', ApplicationCreateView.as_view()),
]


