# otzovik
Мини-сервис, который принимает отзыв и сразу оценивает его настроение.<br>
pip install fastapi uvicorn<br>
Запустите сервер:<br>
uvicorn main:app --reload<br>

Примеры использования:<br>
Добавление отзыва:<br>
Позитивные отзывы:<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Этот продукт просто отличный!"}'<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Хороший сервис."}'<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Самокаты супер!"}'<br>
Негативные отзывы:<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Доставка плохая!"}'<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Ремонт ужасный!"}'<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Зарядка отвратительная!"}'<br>
Нейтральные отзывы:<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Сервис можно улучшить."}'<br>
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Нужно больше самокатов."}'<br>

Пример ответа на добавление отзыва:<br>
{"id":8,"text":"Нужно больше самокатов.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.840350"}<br>

Получение всех отзывов:<br>
curl "http://localhost:8000/reviews"<br>
Ответ:<br>
[{"id":8,"text":"Нужно больше самокатов.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.840350"},{"id":7,"text":"Сервис можно улучшить.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.816835"},{"id":6,"text":"Зарядка отвратительная!","sentiment":"negative","created_at":"2025-07-20T07:40:43.913762"},{"id":5,"text":"Ремонт ужасный!","sentiment":"negative","created_at":"2025-07-20T07:40:43.894002"},{"id":4,"text":"Доставка плохая!","sentiment":"negative","created_at":"2025-07-20T07:40:43.859249"},{"id":3,"text":"Самокаты супер!","sentiment":"positive","created_at":"2025-07-20T07:40:36.631810"},{"id":2,"text":"Хороший сервис.","sentiment":"positive","created_at":"2025-07-20T07:40:36.612049"},{"id":1,"text":"Этот продукт просто отличный!","sentiment":"positive","created_at":"2025-07-20T07:40:36.542513"}]<br>

Получение негативных отзывов:<br>
curl "http://localhost:8000/reviews?sentiment=negative"<br>
Ответ:<br>
[{"id":6,"text":"Зарядка отвратительная!","sentiment":"negative","created_at":"2025-07-20T07:40:43.913762"},{"id":5,"text":"Ремонт ужасный!","sentiment":"negative","created_at":"2025-07-20T07:40:43.894002"},{"id":4,"text":"Доставка плохая!","sentiment":"negative","created_at":"2025-07-20T07:40:43.859249"}]<br>
