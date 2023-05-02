from django.urls import path
from . import views

app_name = 'tmpl'

urlpatterns = [
    path('simple',views.simple),
]