# otzovik
Мини-сервис, который принимает отзыв и сразу оценивает его настроение.
pip install fastapi uvicorn
Запустите сервер:
uvicorn main:app --reload

Примеры использования:
Добавление отзыва:
Позитивные отзывы:
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Этот продукт просто отличный!"}'
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Хороший сервис."}'
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Самокаты супер!"}'
Негативные отзывы:
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Доставка плохая!"}'
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Ремонт ужасный!"}'
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Зарядка отвратительная!"}'
Нейтральные отзывы:
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Сервис можно улучшить."}'
curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"text":"Нужно больше самокатов."}'

Пример ответа на добавление отзыва:
{"id":8,"text":"Нужно больше самокатов.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.840350"}

Получение всех отзывов:
curl "http://localhost:8000/reviews"
Ответ:
[{"id":8,"text":"Нужно больше самокатов.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.840350"},{"id":7,"text":"Сервис можно улучшить.","sentiment":"neutral","created_at":"2025-07-20T07:40:50.816835"},{"id":6,"text":"Зарядка отвратительная!","sentiment":"negative","created_at":"2025-07-20T07:40:43.913762"},{"id":5,"text":"Ремонт ужасный!","sentiment":"negative","created_at":"2025-07-20T07:40:43.894002"},{"id":4,"text":"Доставка плохая!","sentiment":"negative","created_at":"2025-07-20T07:40:43.859249"},{"id":3,"text":"Самокаты супер!","sentiment":"positive","created_at":"2025-07-20T07:40:36.631810"},{"id":2,"text":"Хороший сервис.","sentiment":"positive","created_at":"2025-07-20T07:40:36.612049"},{"id":1,"text":"Этот продукт просто отличный!","sentiment":"positive","created_at":"2025-07-20T07:40:36.542513"}]
Получение негативных отзывов:
curl "http://localhost:8000/reviews?sentiment=negative"
Ответ:
[{"id":6,"text":"Зарядка отвратительная!","sentiment":"negative","created_at":"2025-07-20T07:40:43.913762"},{"id":5,"text":"Ремонт ужасный!","sentiment":"negative","created_at":"2025-07-20T07:40:43.894002"},{"id":4,"text":"Доставка плохая!","sentiment":"negative","created_at":"2025-07-20T07:40:43.859249"}]
