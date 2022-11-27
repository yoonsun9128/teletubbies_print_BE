from rest_framework import serializers
from store.models import Filter
from users.models import User
from ImageStorage.models import Image


class FilterSerializer(serializers.ModelSerializer): #Filter모델 시리얼라이즈
    class Meta:
        model = Filter
        fields = "__all__"

