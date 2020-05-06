import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from blog.base import BaseModel
from .helpers import user_directory_path

class Media(BaseModel):
    id = models.UUIDField(
        _('id'),
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        help_text=_(
            'Media unique code.'
        )
    )

    name = models.CharField(max_length=200)
    data = models.FileField(upload_to=user_directory_path, max_length=500)

    class Meta:
        verbose_name = _('upload')
        verbose_name_plural = _('uploads')

    def __str__(self) -> str:
        return str(self.pk)