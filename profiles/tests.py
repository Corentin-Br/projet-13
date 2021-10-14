from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class LettingsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="admin", password="password12234")
        cls.profile = Profile(
            user=cls.user,
            favorite_city="Paris"
        )
        cls.profile.save()

    def test_title_of_the_index_page_is_correct(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertContains(response, '<title>Profiles</title>')

    def test_title_of_a_letting_page_is_correct(self):
        response = self.client.get(reverse('profile', kwargs={"username": str(self.profile)}))
        self.assertContains(response, f'<title>{self.profile}</title>')
