from django.urls import path
from .views import *

urlpatterns = [
    path('all_films/', render_all_films, name = "all_films"),
    path('add_to_favourite/<int:film_id>/', add_to_favourite, name="add_to_favourite"),
    path('favourites/', render_favourites, name = "favourite_films"),
    path("remove_from_favourite/<int:film_id>/", remove_from_favourite, name="remove_from_favourite")
]