# drf-course-api2

Django REST Framework Series
[https://www.youtube.com/playlist?list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t]

# Video 1 - Part 1

Django REST Framework series - Setup and Models
[https://www.youtube.com/watch?v=6AEvlNgRPNc&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=1]

```
$ python3 -m venv venv-drf
$ source venv-drf/bin/activate
$ pip install -r requirements.txt

$ python manage.py graph_models api > models.dot
```

# Video 2 - Part 1

Django REST Framework - Serializers & Response objects | Browsable API
[https://www.youtube.com/watch?v=BMym71Dwox0&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=2]

# Video 3 - Part 1

Django REST Framework- Nested Serializers, SerializerMethodField and Serializer Relations
[https://www.youtube.com/watch?v=KfSYadIFHgY&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=3]

# Video 3 - Part 2

...

# Video 4 - Part 1

Django REST Framework - Serializer subclasses and Aggregated API data
[https://www.youtube.com/watch?v=_xbI0-mjtw4&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=4]

# Video 5 - Part 1

django-silk for Profiling and Optimization with Django REST Framework
[https://www.youtube.com/watch?v=OG8alXR4bEs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=5]

```
$ pip install django-silk

File: settings.py
INSTALLED_APPS = [
    ...
    'silk' # Django Silk for profiling
]

MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',  # Middleware for Django Silk
]

File: urls.py
urlpatterns = [
    ...
    path('silk/', include('silk.urls', namespace='silk')),
]

$ python manage.py migrate
```

# Video 6 - Part 1

Django REST Framework - Generic Views | ListAPIView & RetrieveAPIView
[https://www.youtube.com/watch?v=vExjSChWPWg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=6]

# Video 7 - Part 1

Django REST Framework - Dynamic Filtering | Overriding get_queryset() method
[https://www.youtube.com/watch?v=3Gi-w4Swge8&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=7]

```
$ python manage.py createsuperuser
```

Current: 1:31

# Video 7 - Part 2

...

# Video 8 - Part 1

Django REST Framework - Permissions and Testing Permissions
[https://www.youtube.com/watch?v=rx5IV_4Iuog&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=8]


# Video 9 - Part 1

Django REST Framework - APIView class
[https://www.youtube.com/watch?v=TVFCU0w65Ak&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=9]

# Video 10 - Part 1

Django REST Framework - Creating Data | ListCreateAPIView and Generic View Internals
[https://www.youtube.com/watch?v=Jh85U1nhMh8&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=10]

Classy Django REST Framework
[https://www.cdrf.co/]

# Video 11 - Part 1

Django REST Framework - Customising permissions in Generic Views | VSCode REST Client extension
[https://www.youtube.com/watch?v=mlQZ1i8rUKQ&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=11]

# Video 12 - Part 1

Django REST Framework - JWT Authentication with djangorestframework-simplejwt
[https://www.youtube.com/watch?v=Xp0-Yy5ow5k&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=12]

Authentication
[https://www.django-rest-framework.org/api-guide/authentication/#authentication]

# Video 12 - Part 2

JSON Web Token Authentication
[https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication]

jazzband/djangorestframework-simplejwt
[https://github.com/jazzband/djangorestframework-simplejwt]

Simple JWT
[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]

# Video 12 - Part 3

```
$ pip install djangorestframework-simplejwt
$ pip freeze > requirements.txt

File: settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

# Video 12 - Part 4

File: drf_course/urls.py
...
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Video 12 - Part 4

Django REST Framework - Refresh Tokens & JWT Authentication
[https://www.youtube.com/watch?v=H3OY36wa7Cs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=13]

# Video 13 - Part 1

Django REST Framework - Refresh Tokens & JWT Authentication
[https://www.youtube.com/watch?v=H3OY36wa7Cs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=13]

Simple JWT / Settings
[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html]

# Video 14 - Part 1

Django REST Framework - Updating & Deleting data
[https://www.youtube.com/watch?v=08gHVFPFuBU&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=14]

# Video 14 - Part 2

...

# Video 15 - Part 1

drf-spectacular - Django REST Framework API Documentation
[https://www.youtube.com/watch?v=E3LUvsPWLwM&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=15]

Documenting your API
[https://www.django-rest-framework.org/topics/documenting-your-api/]

drf-sectacular/github
[https://github.com/tfranzel/drf-spectacular]

drf-spectacular documentation
[https://drf-spectacular.readthedocs.io/en/latest/]

# Video 15 - Part 2

```
$ pip install drf-spectacular
$ pip freeze > requirements.txt

INSTALLED_APPS = [
    # ALL YOUR APPS
    'drf_spectacular',
]

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'E-Commerce API',
    'DESCRIPTION': 'A simple Product & Order API that helps us to learn Django Rest Framework',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

$ ./manage.py spectacular --color --file schema.yml
File: drf_course/urls.py
...
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

Browser
http://localhost:8000/api
http://localhost:8000/api/schema/
http://localhost:8000/api/schema/swagger-ui/
http://localhost:8000/api/schema/redoc/
```

# Video 16 - Part 1

django-filter and DRF API filtering - Django REST Framework
[https://www.youtube.com/watch?v=NDFgTGTI8zg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=16]

Filtering
[https://www.django-rest-framework.org/api-guide/filtering/]
[https://www.django-rest-framework.org/api-guide/filtering/#generic-filtering]
[https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend]


```
$ pip install django-filter
$ pip freeze > requirements.txt

INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

File: views.py
...
filterset_fields = ['name', 'price']
...
```

Browser
[http://localhost:8000/products/?name=Television]
[http://localhost:8000/products/?price=300]

[https://django-filter.readthedocs.io/en/latest/guide/usage.html]

# Video 16 - Part 2

[https://django-filter.readthedocs.io/en/stable/ref/filterset.html#fields]

[http://localhost:8000/products/?price__gt=100]
[http://localhost:8000/products/?price__lt=100]
[http://localhost:8000/products/?price__range=100,350]
[http://localhost:8000/products/?name__contains=lev]
[http://localhost:8000/products/?name__iexact=digital%20camera]

# Video 17 - Part 1

SearchFilter and OrderingFilter in Django REST Framework
[https://www.youtube.com/watch?v=LCYqDsl1WYI&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=17]

[http://localhost:8000/products/?search=vision]

# Video 17 - Part 2

[https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend]
[https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter]

[http://localhost:8000/products/?ordering=price]
[http://localhost:8000/products/?ordering=-price]
[http://localhost:8000/products/?ordering=name]
[http://localhost:8000/products/?ordering=-name]

# Video 18 - Part 1

Writing Filter Backends in Django REST Framework
[https://www.youtube.com/watch?v=u4S71cO5QhI&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=18]

[https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering]

# Video 19 - Part 1

API Pagination - Django REST Framework | PageNumberPagination & LimitOffsetPagination
[https://www.youtube.com/watch?v=sTyMe2R9mzk&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=19]

Pagination
[https://www.django-rest-framework.org/api-guide/pagination/]

[http://localhost:8000/products/?size=3]
[http://localhost:8000/products/?offset=6&limit=4]

# Video 20 - Part 1

Viewsets & Routers in Django REST Framework
[https://www.youtube.com/watch?v=4MrB4IvW6Ow&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=20]

[https://www.django-rest-framework.org/api-guide/viewsets/]
[https://www.django-rest-framework.org/api-guide/routers/]

Classy Django REST Framework
[https://www.cdrf.co/]
[https://www.cdrf.co/3.14/rest_framework.viewsets/ModelViewSet.html]

# Video 21 - Part 1

Viewset Actions, Filtering and Permissions in Django REST Framework
[https://www.youtube.com/watch?v=rekvVrjUMjg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=21]

```
$ pip install isort
$ pip freeze > requirements.txt

$ isort ./api/views.py
```

[http://localhost:8000/orders/?status=Confirmed]
[http://localhost:8000/orders/?status=Pending]
[http://localhost:8000/orders/?created_at__gt=2025-04-22]
[http://localhost:8000/orders/?created_at__lt=2025-04-22]
[http://localhost:8000/orders/?created_at=2025-04-22]

[https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing]

# Video 22 - Part 1

Viewset Permissions | Admin vs. Normal User in Django
[https://www.youtube.com/watch?v=KmYYg1qJKNQ&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=22]

# Video 23 - Part 1

Creating Nested Objects | Overriding serializer create() method in Django REST Framework
[https://www.youtube.com/watch?v=CAq7AKAT7Q0&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=23]

[https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations]

