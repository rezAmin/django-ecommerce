import factory
from factory import django
from products.models import Category, Brand, Product


class CategoryFactory(django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.sequence(lambda n: f'category_{n}')


class BrandFactory(django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.sequence(lambda n: f'brand_{n}')


class ProductFactory(django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'test_product'
    description = 'test_description'
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
