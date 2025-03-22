from django import template
from film_app.models import Film

# Об'єкт, що відповідає за реєстрацію тегу
register = template.Library()

# реєструємо simple тег (тег, що просто повертає якесь значення)
@register.simple_tag(name= "count_favourite_films")
def count_favourite_films(request):
    '''Тег повертає кількість улюблених фільмів, що збергіаються у куках'''
    # Число улюблених фільмів
    count_favourite_films = ""
    # Отримуєм cookies улюблених фільмів
    favourites_from_cookie = request.COOKIES.get('favourite_film')
    # якщо кукі є то:
    if favourites_from_cookie:
        # Розділяємо рядок по пробілам, утсорюючи список
        favourite_films_list = favourites_from_cookie.split(" ")
        # отримуєм кількість улюбених фільмів
        count_favourite_films = f" ({len(favourite_films_list)})"
    # повертаємо кількість улюбених фільмів
    return count_favourite_films

# реєструємо inclusion_tag (тег, що генерує, html код), який прив'язан до best_film.html
@register.inclusion_tag("film_app/inclusion_tags/best_film.html")
# створюємо функцію тегу best_film, який генерує блок з кращим фільмом
def best_film():
    #створюємо змінну film яка бере об'єкт фільму з бази данних за допомогою pk
    film = Film.objects.get(pk = 1)
    # повертаємо змінну film у best_film.html
    return {"film": film}

# реєструемо inclusion tag (тег, що генерує, html код. Цей тег отримує context з views)
@register.inclusion_tag("film_app/inclusion_tags/film_list_info.html", takes_context=True)
# створюємо функцію-тегу яка, генерує список фільмів, відображаючи іфнормацію про кожен з них
def film_list_info(context):
    # Отримуємо з context list films
    list_films = context["list_films"]
    # Отримуємо з context is_page_favourite
    is_page_favourites = context['is_page_favourites']
    # передаємо параметри які будемо використовувати в film_list_info.html
    return {"list_films": list_films,
            'is_page_favourites': is_page_favourites}