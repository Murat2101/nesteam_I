from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import GameFactory, GenreFactory
from .models import *


class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        Genre(
            name='test genre 1',
            description="test descr 1"
        ).save()

        Studio(
            name="test studio 1",
            workers_count=123,
            games_count=45
        ).save()

        data = {
            "name": "Test game 1",
            "year": 2019,
            "genre": 1,
            "studio": 1
        }

        response = self.client.post('/game-create/', data)
        self.assertEqual(response.status_code, 201)

        game = Game.objects.last()
        self.assertEqual(game.name, data["name"])
        self.assertEqual(game.year, data["year"])
        self.assertEqual(game.genre.id, data["genre"])
        self.assertEqual(game.studio.id, data["studio"])

    def test_create_game_with_wrong_data_should_fail(self):
        response = self.client.post('/game-create/', {"test1": "lorem"})
        self.assertEqual(response.status_code, 400)

    def test_create_game_via_get_request_should_return_405(self):
        data = {
            "name": "Wrong form",
            "year": 2019,
            "genre": 1,
            "studio": 1
        }
        response = self.client.get('/game-create/', data)
        self.assertEqual(response.status_code, 405)
        games_exists = Game.objects.filter(name="Wrong form").exists()
        self.assertFalse(games_exists)


class GamesTest(APITestCase):
    def setUp(self):
        self.game_1 = GameFactory()
        self.game_2 = GameFactory()
        self.genre = GenreFactory()

    def test_get_list_of_games(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)

    def test_get_one_game(self):
        response = self.client.get(f'/games/{self.game_1.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_get_genre(self):
        response = self.client.get(f'/genres/{self.genre.pk}/')
        self.assertEqual(response.status_code, 200)


from django.test import TestCase

# Create your tests here.
