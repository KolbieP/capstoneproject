from django.test import TestCase
from .models import MenuItem, Booking
# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=18, inventory=89)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 18")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Lenord", seats=5, date="2023-11-27T10:00:00Z")
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Lenord")