from django.contrib import admin

from Cards.models import Card, Collection, Deck

# Register your models here.

admin.site.register((Card, Deck, Collection))