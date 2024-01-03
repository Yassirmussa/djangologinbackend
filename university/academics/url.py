from django.urls import path
from . import views

urlpatterns = [
    path("", views.hellomsg),
    path('getpost', views.example_view),

    # API FOR USER
    path('insertuser', views.insertUser),
    path('getuser', views.getUser),
    path('getuserbyID/<int:UserID>/', views.getUserByID),
    path('updateuser/<int:UserID>/', views.updateUser),
    path('deleteuser/<int:UserID>/', views.deleteUser),

    # LOGIN API
    path('login', views.login),
    # AUTH USER
    path('getauthuser', views.getautUser),
    # log out
    path('logout', views.logout),
    #API FOR PROGRAM
    path('insertprogram', views.insertProgram),
    path('getprogram', views.getProgram),
    path('getprobyID/<int:ProID>/', views.getProgramByID),
    path('updateprogram/<int:ProID>/', views.updateProgram),
    path('deleteprogram/<int:ProID>/', views.deleteProgram),


    # API FOR Todo
    path('inserttodo', views.insertTodo),
    path('gettodo', views.getTodos),
    path('gettodobyID/<int:id>/', views.getTodoById),
    path('updatetodo/<int:id>/', views.updateTodo),
    path('deletetodo/<int:id>/', views.deleteTodo),
    


    # API FOR STUDENT
    path('insertstudent', views.register_student),
    path('updatestudent/<int:StuID>/', views.updateStudent),
    path('deleteAll', views.deleteAllStudent),

    
]