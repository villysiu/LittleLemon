from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=50, inventory=100)
        self.assertEqual("{} : {}".format(item.title, item.price), "IceCream : 50")