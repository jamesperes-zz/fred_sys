from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("avaliacriterios", views.avaliacriterios, name="avaliacriterios"),
    path("avaliarum", views.avaliarum, name="avaliarum"),
    path("avaliardois", views.avaliardois, name="avaliardois"),
    path("avaliartres", views.avaliartres, name="avaliartres"),
    path("resultado", views.resultado, name="resultado"),
] 
