
from os.path import splitext
from typing import Dict, Any, Optional
from uuid import (UUID, uuid4)

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.settings import api_settings

from blog.base import BaseModelSerializer
from blog.stubs import QueryType
from uploads.models import Media

class MediaSerializer(BaseModelSerializer):
    class Meta:
        model = Media
        fields = ('id',
                  'name',
                  'data',
                  'created_at',
                  'convert_to')

    convert_to = serializers.CharField(write_only=True, required=False)

class MediaField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self) -> QueryType[Media]:
        return Media.objects.non_deleted()

    def to_internal_value(self, data: Any) -> None:
        if self.pk_field is not None:
            data = self.pk_field.to_internal_value(data)
        try:
            return self.get_queryset().get(pk=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)

    def to_representation(self, value: Media) -> Optional[UUID]:
        """
        Transform the *outgoing* native value into primitive data.
        """
        media = self.get_queryset().get(id=value.pk)
        if not media:
            return None

        use_url = getattr(self, 'use_url', api_settings.UPLOADED_FILES_USE_URL)

        if use_url:
            if not getattr(media.data, 'url', None):
                # If the file has not been saved it may not have a URL.
                return None
            url = media.data.url
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return media.pk
