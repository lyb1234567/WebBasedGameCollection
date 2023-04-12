from django.test import TestCase
from  customUser.models import User
from  Game.models import GameModel
from  Collection.models import GameCollection
from django.utils import timezone
# Create your tests here.
class GameCollectionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            firstName='Test',
            lastName='User',
            profilePic=None,
            userInfo='Test user for testing purposes.',
            dateOfBirth=timezone.now().date(),
            userType='Player',
            location='Test City'
        )
        self.game = GameModel.objects.create(
                gameName='Test Game',
                gameRate=4.5,
                gamePrice=59.99,
                gameDiscount=0.1,
                gameAge=18,
                gameLabel='Action',
                gamePublishDate=timezone.now().date(),
                gameDescription='A sample test game for testing purposes.'
            )

    def test_create_game_collection(self):
        collection_name = 'Test Collection'
        game_collection = GameCollection.objects.create_game_collection(self.user, self.game, collection_name)
        self.assertEqual(game_collection.user, self.user)
        self.assertEqual(game_collection.game, self.game)
        self.assertEqual(game_collection.collectionName, collection_name)

    def test_read_game_collection(self):
        collection_name1 = 'Test Collection1'
        collection_name2 = 'Test Collection2'
        game_collection1 = GameCollection.objects.create_game_collection(self.user, self.game, collection_name1)
        game_collection2 = GameCollection.objects.create_game_collection(self.user, self.game, collection_name2)
        retrieved_game_collection1 = GameCollection.objects.get_game_collection_by_id(game_collection1.collectionCode)
        retrieved_game_collection2 = GameCollection.objects.get_game_collection_by_id(game_collection2.collectionCode)
        self.assertEqual(retrieved_game_collection1, game_collection1)
        self.assertEqual(retrieved_game_collection2, game_collection2)

    def test_update_game_collection(self):
        collection_name = 'Test Collection'
        new_collection_name = 'Updated Collection'
        game_collection = GameCollection.objects.create_game_collection(self.user, self.game, collection_name)
        updated_game_collection = GameCollection.objects.update_game_collection(game_collection.collectionCode, collectionName=new_collection_name)
        self.assertEqual(updated_game_collection.collectionName, new_collection_name)

    def test_delete_game_collection(self):
        collection_name = 'Test Collection'
        game_collection = GameCollection.objects.create_game_collection(self.user, self.game, collection_name)
        GameCollection.objects.delete_game_collection(game_collection.collectionCode)
        with self.assertRaises(GameCollection.DoesNotExist):
            GameCollection.objects.get_game_collection_by_id(game_collection.collectionCode)
