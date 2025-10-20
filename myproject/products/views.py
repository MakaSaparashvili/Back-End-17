from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPagination
from .filters import ProductFilter

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter




# class ProductListView(generics.ListAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#    pagination_class = CustomPagination

#    filter_backends = [DjangoFilterBackend]
#    filterset_fields = {
#       'category': ['exact'],
#       'price': ['gte', 'lte']}
