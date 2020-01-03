from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='index'),
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemons/<int:pk>/update/',
         views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete/',
         views.PokemonDelete.as_view(), name='pokemons_delete'),
    path('pokemons/<int:pokemon_id>/add_battles/',
         views.add_battles, name='add_battles'),
    path('pokemons/<int:pokemon_id>/add_photo/',
         views.add_photo, name='add_photo'),
    path('pokemons/<int:pokemon_id>/assoc_item/<int:item_id>/',
         views.assoc_item, name='assoc_item'),
    path('items/', views.ItemList.as_view(), name='items_index'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]
