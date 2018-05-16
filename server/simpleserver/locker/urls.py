from django.urls import path

from . import views

urlpatterns = [
    path('', views.OpenClose.as_view(), name='open'),
]
