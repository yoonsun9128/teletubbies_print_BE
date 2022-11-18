from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user 
    
    def validate(self, data):
        email = User.objects.filter(email=data['email'])
        
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password": "비밀번호가 맞지 않습니다"
                })
            
        if not len(data.get("email", "")) >= 2:
            raise serializers.ValidationError(
                detail={"error": "email 길이는 2자리 이상이어야 합니다."}
            )
            
        if not len(data.get("password", "")) >= 2:
            raise serializers.ValidationError(
                detail={"error": "password의 길이는 8자리 이상이어야합니다."}
            )
            
        if email.exists():
            raise serializers.ValidationError('이메일이 이미 존재합니다.')
            
        return data
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['email'] = user.email

        return token