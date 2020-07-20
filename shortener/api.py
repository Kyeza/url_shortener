from rest_framework import viewsets, status
from rest_framework.response import Response

from shortener.models import IdCounter, ShortUrl
from shortener.serializers import ShortUrlSerializer
from shortener.utils import shortener_base62_encoder


class ShortUrlViewSet(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer

    def create(self, request, *args, **kwargs):

        # check if the id generator counter is within range
        obj = None
        try:
            obj = ShortUrl.objects.get(full_url=request.data['full_url'])
        except ShortUrl.DoesNotExist:
            COUNTER = IdCounter.load()
            if COUNTER.current_id in range(COUNTER.start_id, COUNTER.end_id + 1) \
                    or COUNTER.current_id == 0:
                COUNTER.previous_id = COUNTER.current_id
                COUNTER.current_id += 1
                COUNTER.save()

                short_url = shortener_base62_encoder(COUNTER.current_id)
                obj = ShortUrl.objects.create(shortened_url=short_url, full_url=request.data['full_url'])
            else:
                return Response(data={'error': 'unique short_url generator out of range'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            serializer = ShortUrlSerializer(obj)
            if serializer.is_valid:
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
