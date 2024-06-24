from django.urls import path

from academics import views

urlpatterns = [

    
    path('regsiterstudent', views.registerStudent),
    path('getstudent', views.getAllStudent),

    path('sendresearch', views.sendResearch),
    path('getresearch', views.getAllResearch),

    path('sendrecomendation', views.sendRecommendation),
    path('getrecomendation', views.getAllRecommendation),

    path('sendgrade', views.sendGrade),
    path('getgrade', views.getAllResult),

    path('allocate', views.AllocateStudent),
    path('getallocation', views.getAllocation),

    path('signpgo', views.signPGO),
    path('getpgo', views.getPGO),

    path('signexaminer', views.signExaminer),
    path('getexaminer', views.getExaminer),
    # path('deleteexaminer', views.deleteExaminer),

    path('signsupervisor', views.signSupervisor),
    path('getsupervisor', views.getSupervisor),
]