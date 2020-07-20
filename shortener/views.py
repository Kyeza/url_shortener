from django.shortcuts import get_object_or_404, redirect, render

from shortener.models import ShortUrl


def root(request, slug):
    url = get_object_or_404(ShortUrl, shortened_url=slug)

    return redirect(url.full_url)


def index(request):
    return render(request, 'shortener/index.html')
