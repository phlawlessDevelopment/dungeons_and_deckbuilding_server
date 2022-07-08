from pyexpat import model
from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField( max_length=32)
    description = models.TextField()

    class CardSets(models.TextChoices):
        ATTACKS = ('Att', 'Attacks')
        WEAPON = ('Wea', 'Attacks')
        SPELLS = ('Spe', 'Spells')
        MOVEMENT = ('Mov', 'Movement')
        ITEMS = ('Ite', 'Items')
        CLASSFEATURES = ('Cls', 'Class Features')

    card_set = models.CharField(
        max_length=3,
        choices = CardSets.choices,
        default= CardSets.ATTACKS
    )

    def __str__(self) -> str:
        return f'{self.title} - {[s[1] for s in self.CardSets.choices if s[0] == self.card_set][0]}'
class Deck(models.Model):
    title = models.CharField(max_length=16)
    cards = models.ManyToManyField(Card)

    def __str__(self) -> str:
        return self.title

class Collection(models.Model):
    title = models.CharField(max_length=32)
    decks = models.ManyToManyField(Deck)

    def __str__(self) -> str:
        return self.title