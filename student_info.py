import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
import django
django.setup()

from random import *
from testapp.models import Student

def phonenumgen():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

from faker import Faker
fakegen=Faker()
def populate(n):
    for i in range(n):
        frollno= fakegen.random_int(min=1,max=999)
        fname= fakegen.name()
        fdob= fakegen.date()
        fmarks= fakegen.random_int(min=20,max=99)
        femail= fakegen.email()
        fphonenumber= phonenumgen()
        faddress= fakegen.address()
        student_record= Student.objects.get_or_create(rollno=frollno,
        name=fname,
        dob=fdob,
        marks=fmarks,
        email=femail,
        phone_no=fphonenumber,
        address=faddress)

n = int(input('Enter no of recoreds you want to insert: '))
populate(n)
print(f'{n} Records inserted successfully')
