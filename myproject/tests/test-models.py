from django.test import TestCase

from myapp.models import Menu


class MenuTest (TestCase):
    def test_get_item (self):
        item = Menu.objects.create(name= "iceCream",pricr = 80,inventory ="100")
        self.assertEqual(item ,  "IceCream : 80")
