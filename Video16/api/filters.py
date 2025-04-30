import django_filters # type: ignore
from api.models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name', 'price')

