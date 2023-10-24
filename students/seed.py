from students.models import *
from faker import Faker
import random

fake = Faker()


def create_subjects_data():
    student_ids = StudentID.objects.all()
    for id in student_ids:
        subjects = Subject.objects.all()
        for subject in subjects:
            SubjectMarks.objects.create(
                student_id = id,
                subject = subject,
                marks = random.randint(40, 100)
            )


def create_students_data(n=10):
    try:
        for i in range(0, n):
            create_student()
    except Exception as err:
        print(err)


def create_student():
    department_objs = Department.objects.all()
    random_index = random.randint(0, len(department_objs)-1)
    
    student_id = f"STU-0{random.randint(1, 100)}"
    student_name = fake.name()
    student_email = fake.email()
    student_age = random.randint(20, 30)
    student_address = fake.city()
    department = department_objs[random_index]


    student_id_objs = StudentID.objects.create(student_id=student_id)

    Student.objects.create(
        student_id = student_id_objs,
        student_name = student_name,
        student_email = student_email,
        student_age = student_age,
        student_address = student_address,
        department = department
    )