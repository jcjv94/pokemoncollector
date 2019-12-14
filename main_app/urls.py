from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='index'),
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail')
]
