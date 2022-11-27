from django.db import models
from users.models import User
# Create your models here.

class Filter(models.Model):
    filter_image = models.FileField(null=True, blank=True, upload_to="")
    filter_name = models.CharField(max_length=100, default=0)
    class meta:
        db_table = 'filter'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey('ImageStorage.Image', on_delete=models.CASCADE, default=None, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


