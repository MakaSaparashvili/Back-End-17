from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Counts the number of products in the database'

    def handle(self, *args, **kwargs):
        count = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Total Products: {count}'))

