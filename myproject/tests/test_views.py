from audioop import reverse
from django.test import TestCase
from myapp.models import Menu
from django.urls import reverse

class MenuViewTest (TestCase):
    def setup(self):
        item = Menu.objects.create(name='Menu 1', price=10)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [{'name': 'Menu 1', 'price': 10}, {'name': 'Menu 2', 'price': 15}]
        )