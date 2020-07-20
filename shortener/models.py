import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()


class SingletonBaseModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonBaseModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class IdCounter(SingletonBaseModel):
    start_id = models.PositiveIntegerField(default=1)
    end_id = models.PositiveIntegerField(default=1000)
    current_id = models.PositiveIntegerField(default=0)
    previous_id = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Counter'

    def __str__(self):
        return str(self.current_id)


class ShortUrl(BaseModel):
    shortened_url = models.URLField(unique=True, db_index=True, blank=True)
    full_url = models.URLField(unique=True)

    class Meta:
        ordering = ['shortened_url']
        verbose_name = 'ShortURL'
        verbose_name_plural = 'ShortURLs'

    def __str__(self):
        return str(self.shortened_url)

