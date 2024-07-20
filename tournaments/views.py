from rest_framework import viewsets
from .models import Player, Tournament, Match
from .serializers import PlayerSerializer, TournamentSerializer, MatchSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request, tournament_id=None):
        tournament = Tournament.objects.get(id=tournament_id)
        players = tournament.players.annotate(score=Sum('player1_matches__result') + Sum('player2_matches__result'))
        sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
        serializer = PlayerSerializer(sorted_players, many=True)
        return Response(serializer.data)
