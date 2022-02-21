# Create your tests here.
from ecom.views import contactus_view

from django.urls import reverse,resolve



from django.test import Client, SimpleTestCase, TestCase

# Create your tests here.



class Testurls(SimpleTestCase):
    
    def test_resolve_to_Homepage(self):

        url = reverse("ecommerce: contactus")

        resolver = resolve(url)

        self.assertEquals(resolver,contactus_view)

 










