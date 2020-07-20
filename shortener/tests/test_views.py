from django.test import TestCase
from django.urls import reverse

from shortener.models import ShortUrl


class RootViewTestCase(TestCase):

    def setUp(self) -> None:
        self.full_url = 'https://www.google.com/search?q=url+shortener&oq=google+u&aqs=chrome.0.69i59j69i60l3j0j69i57' \
                        '.1069j0j7&sourceid=chrome&ie=UTF-8'
        self.short_url = ShortUrl.objects.create(shortened_url='b', full_url=self.full_url)

    def test_root_view(self):
        url = reverse('shortener:root', args=(self.short_url.shortened_url,))

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302, msg=f'Expected: {302} | Result: {response.status_code}')
        self.assertEqual(response.url, self.full_url, msg=f'Expected: {self.full_url} | Result: {response.url}')


