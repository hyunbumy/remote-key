from django.urls import path

from . import views

urlpatterns = [
    path('', views.OpenCloseView.as_view(), name='open'),
]
