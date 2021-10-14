from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):
    def test_index_works_correctly(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<title>Holiday Homes</title>")
