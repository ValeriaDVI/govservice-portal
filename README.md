#  GovService Portal

Портал державних послуг — веб-застосунок для подачі та відстеження заяв громадянами.

## Технології
- Python / Django 6 / Django REST Framework
- PostgreSQL + Django ORM
- Redis (кешування)
- JWT автентифікація
- Celery (фонові задачі)
- Swagger / OpenAPI документація

## Функціонал
- Реєстрація та вхід (JWT)
- Громадянин подає заяви та відстежує статус
- Держслужбовець переглядає всі заяви
- REST API з повною Swagger документацією
- Адмін панель

## Запуск локально

### 1. Клонуй репозиторій
git clone https://github.com/ValeriaDVI/govservice-portal.git
cd govservice-portal

### 2. Створи віртуальне середовище
python -m venv venv
venv\Scripts\activate

### 3. Встанови залежності
pip install -r requirements.txt

### 4. Створи .env файл
DB_NAME=govservice_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
DEBUG=True

### 5. Запусти міграції
python manage.py migrate

### 6. Запусти сервер
python manage.py runserver

Відкрий http://127.0.0.1:8000