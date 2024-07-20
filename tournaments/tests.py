from django.test import TestCase
from .models import Player, Tournament, Match

class PlayerModelTest(TestCase):
    def setUp(self):
        Player.objects.create(name="John Doe", rating=1500)

    def test_player_creation(self):
        player = Player.objects.get(name="John Doe")
        self.assertEqual(player.rating, 1500)

class TournamentModelTest(TestCase):
    def setUp(self):
        tournament = Tournament.objects.create(name="Test Tournament")
        player1 = Player.objects.create(name="John Doe", rating=1500)
        player2 = Player.objects.create(name="Jane Doe", rating=1400)
        tournament.players.add(player1, player2)

    def test_tournament_creation(self):
        tournament = Tournament.objects.get(name="Test Tournament")
        self.assertEqual(tournament.players.count(), 2)
