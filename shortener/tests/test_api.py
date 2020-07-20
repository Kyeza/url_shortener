from django.test import TestCase

from shortener.models import ShortUrl


class ShortUrlViewSet(TestCase):

    def setUp(self) -> None:
        self.full_url = 'https://www.google.com/search?q=url+shortener&oq=google+u&aqs=chrome.0.69i59j69i60l3j0j69i57' \
                        '.1069j0j7&sourceid=chrome&ie=UTF-8'

    def test_short_url_creation(self):
        url = '/api/short_urls/'

        response = self.client.post(url, data={'full_url': self.full_url})

        num_of_urls_db = ShortUrl.objects.count()
        short_url = ShortUrl.objects.first()

        self.assertEqual(response.status_code, 201, msg=f'Expected: {201} | Result: {response.status_code}')
        self.assertEqual(num_of_urls_db, 1, msg=f'Expected: {1} | Result: {num_of_urls_db}')
        self.assertIsInstance(short_url, ShortUrl)
        self.assertEqual(short_url.full_url, self.full_url,
                         msg=f'Expected: {self.full_url} | Result: {short_url.full_url}')
