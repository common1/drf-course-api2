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

