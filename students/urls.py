from django.urls import path
import students.views as views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/add/', views.add_student, name='add_student'),
    path('course/add/', views.add_course, name='add_course'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]