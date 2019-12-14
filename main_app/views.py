from django.shortcuts import render

from .models import Pokemon


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
    return render(request, 'pokemons/detail.html', { 'pokemon': pokemon })