from restaurant.models import MenuItem
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        item = MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        item = MenuItem.objects.create(title="Buffalo Wings", price=10, inventory=30)
        

    def test_getall(self):
        icecream = MenuItem.objects.get(title="Ice Cream")
        buffalowings = MenuItem.objects.get(title="Buffalo Wings")
        # print(buffalowings)
        # print(icecream.price)
        self.assertEqual("{} : {}".format(icecream.title, icecream.price), "Ice Cream : 80.00")
        self.assertEqual("{} : {}".format(buffalowings.title, buffalowings.price), "Buffalo Wings : 10.00")