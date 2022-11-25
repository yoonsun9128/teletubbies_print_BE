from django.db import models
from users.models import User
# Create your models here.

class Filter(models.Model):
    filter_image = models.ImageField()
    bookmark = models.ManyToManyField(User, related_name='bookmark_filter')

    class meta:
        db_table = 'filter'


class Filter_option(models.Model):
    SIZE = 'SIZE'
    OPTION = 'OPTION'
    TYPE_CHOICES = (
        (SIZE, 'size'),
        (OPTION, 'option')
    )

    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    value = models.CharField(max_length=100) # size=6x8 / size=8x10 / 달력
    price = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES) #초이스 속성 주고 , 얘가 size 인지 option 선택하는 곳


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    review_image = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


