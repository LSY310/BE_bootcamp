from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.AddressList.as_view()), # api/v1/users
    path("<int:user_id>",  views.Address_Detail.as_view()),
    path('<int:pk>/update', views.UpdateAddress.as_view(), name='update-address'),
    path('<int:pk>/delete', views.DeleteAddress.as_view(), name='delete-address'),
    path("getToken", obtain_auth_token), # username,password를 보내면 토큰을 반환
    path("/login/simpleJWT", TokenObtainPairView.as_view()),#코드 추가 부분
    path("/login/simpleJWT/refresh", TokenRefreshView.as_view()),#코드 추가 부분
    path("/login/simpleJWT/verify", TokenVerifyView.as_view())#코드 추가 부분
]
