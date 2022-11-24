from django.db import models
import users


class Image(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    # type = models.CharField(max_length=100, choices=(('INPUT', 'INPUT'), ('OUTPUT', 'OUTPUT')))
    input_img = models.FileField("입력사진", blank=True, null=True, upload_to="input/")
    output_img = models.FileField("결과사진", blank=True , null=True, upload_to="output/")
    # url = models.ImageField(upload_to="")