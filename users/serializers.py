from rest_framework import serializers
from users.models import User
from ImageStorage.models import Image
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from store.serializers import FilterSerializer, ReviewSerializer, OptionReviewSerializer, OrderCreateSerializer

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)


    class Meta:
        model = User
        fields = ('email','username','phone_number', 'address', 'password','password2')
        extra_kwargs={
            'password':{'write_only':True}
        }
        
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
        password=data.get('password')
        password2=data.pop('password2')
        if password != password2:
            raise serializers.ValidationError(
                detail={"error":"비밀번호가 맞지 않습니다"}
            )
                
            
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
    
class UserMypageSerializer(serializers.ModelSerializer): #user(username, reward), 주문내역(size,달력,가격,주문날짜,주문번호), 장바구니(구매옵션설정페이지), 나의리뷰(리뷰내용), 북마크필터조회(북마크한 필터이미지)
    order_create_set = OrderCreateSerializer(many=True) #주문내역
    order_option_set = OptionReviewSerializer(many=True) #장바구니
    bookmark_set = FilterSerializer(many=True) # 북마크 + filter_image
    review_set = ReviewSerializer(many=True) # 리뷰내용(리뷰이미지, 내용, 리뷰작성일자)

    class meta:
        model = User
        fields = ("username", "reward",)

class UserInfoModSerializer(serializers.ModelSerializer): #이메일, 비밀번호, 유저네임, 핸드폰, 주소 ******************************얘 좀 이상함*************************
    class meta:
        model = User
        fields = ('email','username','phone_number', 'address', 'password','password2')
        
