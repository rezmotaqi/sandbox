from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TagOwner(models.Model):
    owner = models.CharField(max_length=20)


class TypeTag(models.Model):

    value = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)


    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return f'{self.value}/{self.content_type}/{self.object_id}'


class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    tag = GenericRelation('TypeTag')


class News(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(max_length=500, null=True)
    tag = GenericRelation('TypeTag')
