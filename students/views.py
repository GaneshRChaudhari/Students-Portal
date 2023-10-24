from django.shortcuts import render, redirect
from students.models import *
# Create your views here.
from students.seed import create_student

from django.core.paginator import Paginator

def students(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    total_users = Student.objects.all().count()
    original_count = Student.admin_objects.all().count()
    return render(request, 'students.html', {'students': page_obj, 'total_users': total_users, 'original_count': original_count})


def add_student(request):
    create_student()
    return redirect(students)


def get_marks(request, student_id):
    print("student id is:++++++++++++++++++++ ", student_id)
    queryset = SubjectMarks.objects.filter(student_id__student_id = student_id)
    total = queryset.aggregate(total_marks=models.Sum('marks'))
    print("marks for student---------------", queryset)
    return render(request, 'marks.html', {'marks': queryset, 'id': student_id, 'total_marks': total})


def delete_student(request, student_id):
    all_students = Student.objects.filter(student_id__student_id = student_id)
    all_students[0].is_deleted = True
    all_students[0].save()
    
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    total_users = Student.objects.all().count()
    original_count = Student.admin_objects.all().count()
    print("student deleted=================================")
    return render(request, 'students.html', {'students': page_obj, 'total_users': total_users, 'original_count': original_count})


