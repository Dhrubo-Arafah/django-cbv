from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('all-students/', views.StudentView.as_view(), name='all_students'),
    path('add-student/', views.AddStudent.as_view(), name='add_student'),
    path('student-detail/<pk>', views.StudentDetail.as_view(), name='student-detail'),
    path('update-student/<pk>', views.UpdateStudent.as_view(), name='update-student'),
    path('delete-student/<pk>', views.DeleteStudent.as_view(), name='delete-student'),
]
