from rest_framework import serializers

from shortener.models import IdCounter, ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = [
            'shortened_url', 'full_url'
        ]
        extra_kwargs = {
            'shortened_url': {'read_only': True}
        }
