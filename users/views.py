from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView, )
from .models import User

from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserMypageSerializer, UserInfoModSerializer, ReviewCreateSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class UserMypageView(APIView): #북마크, 리뷰내용, 주문내역
    def get(self, request, user_id):
        user = User.objects.get(id=user_id) 
        serializer = UserMypageSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)        
        
class UserDetailView(APIView): #이메일, 비밀번호, 유저네임, 핸드폰, 주소
    def put(self, request, user_id): #정보수정페이지
        user = get_object_or_404(User, id=user_id)
        print(user)
        if request.user.id == user.id:
            serializer = UserInfoModSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
