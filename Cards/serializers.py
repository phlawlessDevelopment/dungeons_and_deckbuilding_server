from rest_framework.serializers import ModelSerializer , PrimaryKeyRelatedField

from Cards.models import Card, Deck


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class DeckSaveSerializer(ModelSerializer):
    cards = PrimaryKeyRelatedField(many=True,queryset=Card.objects.all())
    class Meta:
        model = Deck
        fields = ['title','cards']

class DeckSerializer(ModelSerializer):
    cards = CardSerializer(many=True)
    class Meta:
        model = Deck
        fields = ['title','cards']


class CollectionSerializer(ModelSerializer):
    decks = DeckSaveSerializer(many=True)
    class Meta:
        model = Deck
        fields = ['title','decks']

class CollectionSaveSerializer(ModelSerializer):
    decks = PrimaryKeyRelatedField(many=True,queryset=Deck.objects.all())
    class Meta:
        model = Deck
        fields = ['title','decks']