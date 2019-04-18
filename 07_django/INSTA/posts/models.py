from django.db import models
from django_extensions.db.models import TimeStampedModel
from faker import Faker
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

faker = Faker()

#------------------------------------------------------------------
# import os
# ENV = os.environ.get('ENVIRONMENT', 'development')
#
# # 이렇게 쓰면 사용자가 사용하는 서버에서 사용 안되고 개발할때만 사용하는거
# if ENV == 'development':
#     from faker import Faker


class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            Post.objects.create(content=faker.text(120))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    file = ProcessedImageField( # pip install pillow
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600)],
        # format=['JPEG','GIF'],

        options={'quality': 90},
    )


class Comment(TimeStampedModel):
    comment = models.CharField(max_length=100, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


