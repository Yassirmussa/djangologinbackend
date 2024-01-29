from django.urls import path
from academics import views

urlpatterns = [
    path("", views.hellomsg),
    path('getpost', views.example_view),


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
    path('insertstudent', views.insertStudent),
    path('getstudent', views.getStudent),
    path('updatestudent/<int:StuID>/', views.updateStudent),
    path('deleteAll', views.deleteAllStudent),


    # API FOR COURSE
    path('insertcourse', views.insertCourse),
    path('getcourses', views.getCourse),
    path('getcourseByID/<int:CoID>/', views.getCourseByID),
    path('updatecourse/<int:CoID>/', views.updateCourse),
    path('deletecoourse/<int:CoID>/', views.deleteCourse),
    path('getCourseByProID/<int:ProID>/', views.getCourseByProID),
       
]