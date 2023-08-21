from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Tag(models.Model):
    lable = models.CharField(max_length = 255)

class TaggedItems(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE) 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    