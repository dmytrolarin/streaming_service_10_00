$(document).ready(function(){
    // Отримуємо форму по id та встановлюємо подію відправки форми 
    $("#reviewForm").submit(function(event){
        // Запобігаємо стандартній поведінці (запобігаємо відправці форми та перезавантаженню сторінки)
        event.preventDefault();
        // Формуємо AJAX-запит
        $.ajax({
            type: 'post', // Вказуємо тип запиту як post
            data: $(this).serialize(), // Отримуємо усі поля цієї (this) форми у форматі пар ключ=значення
            success: function(){
                console.log('success')
            }
        })
    });

});