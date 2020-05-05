from django.db import models
from blog.base import BaseModel

class Tag(BaseModel):
    name_eng = models.CharField(max_length=100)
    name_rus = models.CharField(max_length=100)

class Post(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    #author
    #preview_image
    #images
    #tags
    
    class Meta:
        ordering = ('-created_at',)