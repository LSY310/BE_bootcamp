from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.authentication import TokenAuthentication # 사용자 인증 (추가)
from rest_framework.permissions import IsAuthenticated # 권한 부여 (추가)
class Users(APIView):
    
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data = request.data)
        try :
            validate_password(password)
        except :
            raise Response(serializer.errors)
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else :
            raise Response(serializer.errors)
        
# api/v1/users/myinfo [GET,PUT]
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication] # 추가
    permission_classes = [IsAuthenticated] # 추가
    # read
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    # update
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)