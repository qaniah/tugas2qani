from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class MyWatchListTests(TestCase):
    def test_html_url(self):
        response = Client().get(reverse("mywatchlist:show_mywatchlist"))
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        response = Client().get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = Client().get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)