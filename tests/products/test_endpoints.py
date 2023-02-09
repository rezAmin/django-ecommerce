import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndPoints:

    endpoint = '/api/category/'

    def test_category_get(self, category_factory, api_clint):
        category_factory.create_batch(4)

        response = api_clint().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndPoints:

    endpoint = '/api/brand/'

    def test_brand_get(self, brand_factory, api_clint):
        brand_factory.create_batch(4)

        response = api_clint().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndPoints:

    endpoint = '/api/product/'

    def test_product_get(self, product_factory, api_clint):
        product_factory.create_batch(4)

        response = api_clint().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
