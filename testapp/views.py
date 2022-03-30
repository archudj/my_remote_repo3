from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def student_view(request):
    #student_list = Student.objects.all()
    student_list = Student.objects.filter(marks__lt=35)
    mydict={'student_list':student_list}

    return render(request,'testapp/student.html',mydict)
