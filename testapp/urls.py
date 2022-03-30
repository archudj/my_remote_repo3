from django.urls import path
from testapp import views

urlpatterns = [
    path('studentsdata/', views.student_view),
]
