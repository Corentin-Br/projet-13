from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address(
            number=5,
            street="Advance Street",
            city="Helena",
            state="MT",
            zip_code="33058",
            country_iso_code="USA"
        )
        cls.address.save()
        cls.letting = Letting(
            title="Letting of Montana",
            address=cls.address
        )
        cls.letting.save()

    def test_title_of_the_index_page_is_correct(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertContains(response, '<title>Lettings</title>')

    def test_title_of_a_letting_page_is_correct(self):
        response = self.client.get(reverse('letting', kwargs={"letting_id": self.letting.pk}))
        self.assertContains(response, f'<title>{self.letting.title}</title>')



