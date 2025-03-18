from django import template

# 
register = template.Library()

# 
@register.simple_tag(name= "count_favourite_films")
def count_favourite_films(request):
    # 
    count_favourite_films = ""
    # 
    favourites_from_cookie = request.COOKIES.get('favourite_film')
    # 
    if favourites_from_cookie:
        # 
        favourite_films_list = favourites_from_cookie.split(" ")
        # 
        count_favourite_films = f" ({len(favourite_films_list)})"
    # 
    return count_favourite_films