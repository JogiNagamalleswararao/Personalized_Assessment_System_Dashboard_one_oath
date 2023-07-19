from django.urls import path
from . import views
urlpatterns=[
    #path('', views.splash, name='splash'),
    path('',views.base,name='base'),
    path('login/',views.login,name='login'),
    path('student_r/',views.student_r,name='student_r'),
    path('teacher_r/',views.teacher_r,name='teacher_r'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('create_assessment', views.create_assessment, name='create_assessment'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('start_assignment/<int:assignment_id>/', views.start_assignment, name='start_assignment'),
    # path('submit_assignment/<int:assignment_id>/', views.submit_assessment, name='submit_assignment'),
    path('submit_assessment/<int:assignment_id>/', views.submit_assessment, name='submit_assessment'),
    path('logout/', views.logout, name='logout'),

]