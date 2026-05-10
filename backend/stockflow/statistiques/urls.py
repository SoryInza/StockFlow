from django.urls import path

from .views import statistiques

urlpatterns = [

    path(
        'statistiques',
        statistiques
    ),
]