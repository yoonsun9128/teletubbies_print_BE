from django.db import models
from store.models import Filter
from users.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter = models.ForeignKey(Filter, null=True, on_delete=models.CASCADE)
    input_img = models.FileField("입력사진", blank=True, null=True, upload_to="input/")
    output_img = models.FileField("결과사진", blank=True , null=True, upload_to="output/")
    likes = models.ManyToManyField(User, related_name="likes_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)