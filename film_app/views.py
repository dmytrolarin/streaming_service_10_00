from django.shortcuts import render, redirect
from .models import Film
# Create your views here.

def render_all_films(request):
    all_films = Film.objects.all()
    return render(request, "film_app/all_films.html", {"list_films" : all_films, 'is_page_favourites':False})

# Функція додає фільм в улюблені через кукі.
def add_to_favourite(request, film_id):
    # Стоврення об'єкту відповіді (ця відповідь перенаправляє користувача на сторінку з усіма фільмами)
    response = redirect("all_films")
    #  Отримує рядок з pk (id) улюблених фільмів з кукі 
    favourites_from_cookie = request.COOKIES.get('favourite_film')
    #Якщо немає куків (якщо у користувача не збережно улюблені фільми)
    if not favourites_from_cookie:
        # Зберігаємо кукі з pk улюблених фільмів та задаємо параметр max_age, який відповідає за "час життя" куків у секундах
        response.set_cookie("favourite_film", film_id, max_age= 3600)
    else:
        
        # Конвертуємо рядок у список з pk улюблених фільмів
        favourites_list = favourites_from_cookie.split(' ')
        # створюємо умову яка первіряе чи pk фільму є у списку
        if str(film_id) not in favourites_list:
            # додаемо pk нового улюбленого фільм у рядок для кукі
            updated_cookie = f"{favourites_from_cookie} {film_id}"
            # оновлюємо кукі
            response.set_cookie("favourite_film", updated_cookie, max_age= 3600)
    # Повертаємо відповідь
    return response

#створюємо функцію render_favourites, що відповідає за генерацію сторінки з улюбленими фільмами
def render_favourites(request):
    # отримуємо рядок з pk улюблених фільмів з кукі
    favourites_from_cookie = request.COOKIES.get('favourite_film')
    # створюємо порожній список favourite_films
    favourite_films = []
    # Перевіряємо, чи є файли cookie улюблених фільмів
    if favourites_from_cookie:
        # Конвертуємо рядок у список з pk улюблених фільмів
        favourites_list_pks = favourites_from_cookie.split(' ')
        # Беремо  об'єкти з моделі Film, якщо їх pk є в списку
        favourite_films = Film.objects.filter(pk__in = favourites_list_pks)
    # Рендеримо сторінку
    return render(request, "film_app/favourites.html", context={'list_films': favourite_films, 'is_page_favourites':True})