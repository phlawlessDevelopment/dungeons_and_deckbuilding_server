from rest_framework.routers import DefaultRouter
from Cards.views import CardViewSet, CollectionViewSet, DeckViewSet

router = DefaultRouter()

router.register(r'cards' , CardViewSet)
router.register(r'decks' , DeckViewSet)
router.register(r'collections' , CollectionViewSet)