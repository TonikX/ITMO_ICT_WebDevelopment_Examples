# Пример работы со SWAGGER 
### Старт проекта
1. docker-compose build
2. docker-compose up

### Установка swagger
0. ```pip install drf_yasg```
1. В settings.py в переменную INSTALLED_APPS дописываем 'drf_yasg' и он должен выглядеть так:

```python
# settings.py
# ...
INSTALLED_APPS = [
    ...,
    'drf_yasg'
]
# ...
```
2. Добавляем роутинг в urls.py (проекта)

Инициализируем зависмости
```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
```

Создаем view 
```python
schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
```

И добавляем роутинг
```python
urlpatterns = [
    ...,
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
```

