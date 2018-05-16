from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.OpenCloseView.as_view(), name='open'),
]

urlpatterns = format_suffix_patterns(urlpatterns)