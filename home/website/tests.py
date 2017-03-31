from test_plus.test import TestCase
from .models import HomePage


class HomePageTests(TestCase):

    def test_en_by_default(self):
        response = self.get('/')
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, '/en/')

        languages = (('bg', 'Bulgarian'), ('en', 'English'))
        self.assertEqual(languages, response.context['LANGUAGES'])
        self.assertEqual('en', response.context['LANGUAGE_CODE'])

    def test_redirect_to_en_by_default(self):
        response = self.get('/about/')
        self.assertEqual(302, response.status_code)

        # Status code is 404 because /about don't exist
        self.assertRedirects(response, '/en/about/', target_status_code=404)

        languages = (('bg', 'Bulgarian'), ('en', 'English'))
        self.assertEqual(languages, response.context['LANGUAGES'])
        self.assertEqual('en', response.context['LANGUAGE_CODE'])

    def test_switch_to_bulgarian(self):
        response = self.get('/bg/')

        self.assertEqual(200, response.status_code)
        self.assertEqual('bg', response.context['LANGUAGE_CODE'])
