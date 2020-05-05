
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_filters import CharFilter
from django_filters.rest_framework import BaseInFilter, NumberFilter, UUIDFilter
from rest_framework import mixins, serializers

from starcourse.stubs import QueryType

class MarkAsDeletedMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance: 'Type[BaseModel]') -> None:
        instance.deleted_at = timezone.now()
        instance.save()


class DeletedManagerMixin(models.Manager):
    def non_deleted(self) -> 'QueryType[Type[BaseModel]]':
        return self.filter(deleted_at=None)

    def deleted(self) -> 'QueryType[Type[BaseModel]]':
        return self.exclude(deleted_at=None)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        _('create time'),
        auto_now_add=True,
        help_text=_(
            'Time when instance was created.'
        ),
    )
    deleted_at = models.DateTimeField(
        _('delete time'),
        blank=True,
        null=True,
        help_text=_(
            'Time when instance was deleted.'
        ),
    )
    last_update_at = models.DateTimeField(
        _('last update'),
        blank=True,
        null=True,
        help_text=_(
            'Time when isinstance was updted.'
        ),
        auto_now=True
    )

    operation_by = None

    objects = DeletedManagerMixin()


class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True)
    deleted_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True)
    last_update_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ", read_only=True)