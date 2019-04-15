from django.db import models
from  django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

# Create your models here.


class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()



class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True # 마이그레이션엔 영향 안받음



class Writer(TimeStamp):
    name = models.CharField(max_length=100, default='')


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, default='', unique=True)
    description = models.TextField(default='')


class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
