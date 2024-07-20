from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=1200)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    players = models.ManyToManyField(Player, related_name='tournaments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    round_number = models.IntegerField()
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2_matches')
    result = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Round {self.round_number}: {self.player1} vs {self.player2}"

def swiss_pairings(players):
    sorted_players = sorted(players, key=lambda x: (x['score'], x['rating']), reverse=True)
    pairings = []
    for i in range(0, len(sorted_players), 2):
        if i + 1 < len(sorted_players):
            pairings.append((sorted_players[i], sorted_players[i + 1]))
    return pairings
