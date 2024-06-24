from django.urls import path
from account import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
 

urlpatterns = [
    # path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login',views.login),

    path('registeruser', views.insertUser),
    path('getuser', views.getUser),
    path('getuserbyID/<int:UserID>/', views.getUserByID),
    path('updateuser/<int:UserID>/', views.updateUser),
    path('deleteuser/<int:UserID>/', views.deleteUser),

    # path('deleteusers', views.deleteusers),

    # # log out
    # path('logout', views.logout),

]