from django.urls import path
from account import views

urlpatterns = [

    path('msg',views.msg),
    # API FOR USER
    path('insertuser', views.insertUser),
    path('getuser', views.getUser),
    path('getuserbyID/<int:UserID>/', views.getUserByID),
    path('updateuser/<int:UserID>/', views.updateUser),
    path('deleteuser/<int:UserID>/', views.deleteUser),

    # LOGIN API
    path('login', views.login),
    # AUTH USER
    path('getauthuser', views.getauthUser),
    # log out
    path('logout', views.logout),
]