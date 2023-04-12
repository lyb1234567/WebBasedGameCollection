from django.test import TestCase
from django.utils import timezone
from .models import GameModel

class GameModelTestCase(TestCase):
    def setUp(self):
        self.game = GameModel.objects.create(
            gameName='Test Game',
            gameRate=4.5,
            gamePrice=49.99,
            gameDiscount=10.0,
            gameAge=16,
            gameLabel='Action',
            gamePublishDate=timezone.now(),
            gameDescription='Test game description'
        )

    def test_create_game(self):
        game = GameModel.objects.create(
            gameName='New Game',
            gameRate=4.2,
            gamePrice=29.99,
            gameDiscount=5.0,
            gameAge=12,
            gameLabel='Puzzle',
            gamePublishDate=timezone.now(),
            gameDescription='New game description'
        )
        self.assertIsInstance(game, GameModel)
        self.assertEqual(game.gameName, 'New Game')

    def test_read_game(self):
        game = GameModel.objects.get(gameCode=self.game.gameCode)
        self.assertEqual(game.gameName, 'Test Game')

    def test_update_game(self):
        self.game.gameName = 'Updated Game'
        self.game.save()
        game = GameModel.objects.get(gameCode=self.game.gameCode)
        self.assertEqual(game.gameName, 'Updated Game')

    def test_delete_game(self):
        game = GameModel.objects.create(
            gameName='Delete Game',
            gameRate=3.7,
            gamePrice=9.99,
            gameDiscount=0,
            gameAge=6,
            gameLabel='Adventure',
            gamePublishDate=timezone.now(),
            gameDescription='Delete game description'
        )
        game.delete()
        with self.assertRaises(GameModel.DoesNotExist):
            GameModel.objects.get(gameCode=game.gameCode)
