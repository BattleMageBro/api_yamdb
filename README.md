Api_YaMBd это  Rest Api для сервиса YaMBd.
Проект YaMBd собирает отзывы на произведения: книги, фильмы, музыка.
Пользователи могут зарегестрироваться на YaMBd c помощью API. Для этого пользователь должен отправить запрос с Email-ом на адрес '/api/v1/auth/email/'.
Информацию об аккаунте ввсегда можно изменить на '/api/v1/users/'
Посмотреть информацию о категориях или жанрах можно по адресам '/api/v1/categories/', '/api/v1/genres/'.
Чтобы увидеть конкретную категорию, или жанр нужно знать название ссылки. Пользоваться надо адресами '/api/v1/categories/ссылка/', '/api/v1/genres/ссылка/'
Посмотреть информацию о произведенях можно по адресу '/api/v1/titles/'
Конкретное произведение по адресу '/api/v1/titles/название произведения/'
На странице конкретного произведения вы увидите отзывы, рейтинг произведения, и комментарии пользователей. Если вы хотите посмотреть что то отдельно, это можно сделать по адресам
'/api/v1/titles/название произведения/reviews/' - отзывы на кокнретное произведение. '/api/v1/titles/название произведения/comments/' - комментарии.

