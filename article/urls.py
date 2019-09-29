from django.urls import path
from . import views

urlpatterns = [
    path("",views.articlelist),
    path("addarticle/",views.addarticle),
]
