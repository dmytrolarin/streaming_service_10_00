// Коли документ буде готовий (повністю завантажиться)
$(document).ready(function(){
    // Отримуємо усі кнопки та кожній кнопці застосовуємо функцію
    $(".edit-favourite").each(function(){
        // Обробка події, що спрацює при натисканні на кнопку
        $(this).on("click",function(){
            // Формуємо AJAX-запит
            $.ajax({
                // Вказуємо url, на який AJAX робитиме запит. Беремо url з атрибуту value поточної кнопки
                url: $(this).val(),
                // Вказуємо тип запиту
                type: "get",
                // Функція, що відпрацює при відповіді від сервера про успіх
                success: function(response){
                    // Отримуємо кількість улюблених фільмів з відповіді сервера
                    let countFavouriteFilms = response["count_favourite_films"];
                    // Отримуємо HTML-елемент, що відповідає за к-ть улюблених фільмів, та перезаписуємо HTML-вміст цього елементу
                    $("#countFavouriteFilms").html(countFavouriteFilms);
                }
            });
        });
    });
});