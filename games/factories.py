import factory
from .models import Game, Genre
from usersapp.models import UserFactory


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(lambda g: f'Test game {g}')
    year = 2010




class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda gen: f'Test genre {gen}')
    description = 'test description'