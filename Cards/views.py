import csv
import os
from urllib import request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Cards.models import Card, Collection, Deck
from Cards.serializers import CardSerializer, CollectionSaveSerializer, CollectionSerializer, DeckSaveSerializer, DeckSerializer

# Create your views here.

def parse_csv(request):
    with open('seed_data.csv', 'r') as csv_file:
        csv_dicts = list(csv.DictReader(csv_file ,delimiter=','))

        print(csv_dicts)
        for d in csv_dicts:
            d['title'] = d.pop('Card Name')
            d['description'] = d.pop('Effect')
            d['card_set'] = d.pop('Card Set').capitalize()[:3]
            Card.objects.create(**d)
    return Response(None,200)

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class DeckViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DeckSaveSerializer
        return DeckSerializer
    queryset = Deck.objects.all()


class CollectionViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CollectionSaveSerializer
        return CollectionSerializer
    queryset = Collection.objects.all()
