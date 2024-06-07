from django.urls import path
from . import views

urlpatterns = [
    path("", views.AddressList.as_view()), # api/v1/users
    path("<int:user_id>",  views.Address_Detail.as_view()),
    path('<int:pk>/update', views.UpdateAddress.as_view(), name='update-address'),
    path('<int:pk>/delete', views.DeleteAddress.as_view(), name='delete-address'),
]