from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("criterios", views.criterios, name="criterios"),
    path("alternativas", views.alternativas, name="alternativas"),
    path("avaliacriterios", views.avalia_criterios, name="avaliacriterios"),
] 
