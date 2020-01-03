from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item, Photo
from .forms import BattlesForm
import uuid
import boto3


# class Pokemon:
#     def __init__(self, name, attribute, description, level):
#         self.name = name
#         self.attribute = attribute
#         self.description = description
#         self.level = level


# pokemons = [
#     Pokemon('Pikachu', 'Electric',
#             'It can generate electric attacks from the electric pouches located in both of its cheeks', 100),
#     Pokemon('Bulbasaur', 'Grass/Poison',
#             'Known as the Seed Pokémon, Bulbasaur resembles a small, squating dinosaur that walks on four legs and has a large plant bulb on its back.', 15),
#     Pokemon('Squirtle', 'Water', 'Its rounded shape and the grooves on its surface minimize resistance in water, enabling SQUIRTLE to swim at high speeds. It shelters itself in its shell, then strikes back with spouts of water at every opportunity.', 40),
#     Pokemon('Charmander', 'Fire', 'The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokémon becomes enraged, the flame burns fiercely.', 36),
# ]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/index.html', {'pokemons': pokemons})


def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(
        id__in=pokemon.items.all().values_list('id'))
    battles_form = BattlesForm()
    return render(request, 'pokemons/detail.html', {
        'pokemon': pokemon, 'battles_form': battles_form,
        'items': items_pokemon_doesnt_have
    })


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemons/'


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['level', 'attribute', 'description']


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons/'


def add_battles(request, pokemon_id):
    form = BattlesForm(request.POST)
    if form.is_valid():
        new_battles = form.save(commit=False)
        new_battles.pokemon_id = pokemon_id
        new_battles.save()
    return redirect('detail', pokemon_id=pokemon_id)


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'


class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'color', 'ability']


class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'


def assoc_item(request, pokemon_id, item_id):
    # Note that you can pass a toy's id instead of the whole object
    Pokemon.objects.get(id=pokemon_id).items.add(item_id)
    return redirect('detail', pokemon_id=pokemon_id)


def add_photo(request, pokemon_id):
    S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
    BUCKET = 'pokemoncollectr'
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, pokemon_id=pokemon_id)
            photo.save()
        except:
            print('An Error occurred uploading file to S3')
    return redirect('detail', pokemon_id=pokemon_id)
