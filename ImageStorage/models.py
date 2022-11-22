from django.db import models
import users

class Image(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order = models.ForeignKey('users.order', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=(('INPUT', 'INPUT'), ('OUTPUT', 'OUTPUT')))
    url = models.ImageField(upload_to="")
    