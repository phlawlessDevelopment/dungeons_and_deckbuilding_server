from django.contrib import admin
from django.db import router
from django.urls import include, path
from Cards.routers import router as card_router
from Cards.views import parse_csv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv/', parse_csv),
    path('', include(card_router.urls)),
]
