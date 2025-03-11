from django.urls import path
from .views import *

urlpatterns = [
    path('all_films/', render_all_films, name = "all_films"),
    path('add_to_favourite/<int:film_id>/', add_to_favourite, name="add_to_favourite"),
    path('favourites/', render_favourites, name = "favourites_films"),
]