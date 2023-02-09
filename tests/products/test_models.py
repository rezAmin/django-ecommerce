import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_category_output(self, category_factory):
        test = category_factory(name='test_category')

        assert test.__str__() == 'test_category'



class TestBrandModel:
    def test_brand_output(self, brand_factory):
        test = brand_factory(name='test_brand')
        assert test.__str__() == 'test_brand'


class TestProductModel:
    def test_product_output(self, product_factory):
        test = product_factory(name='test_product')
        assert test.__str__() == 'test_product'
