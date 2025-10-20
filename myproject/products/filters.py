import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(
        choices=lambda: [(c, c) for c in Product.objects.values_list('category', flat=True).distinct() if c],
        label='Category',
    )

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gte', 'lte']
        }
