from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['department_name']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    

class Student(models.Model):
    student_id = models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, null=False)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
        

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    

class SubjectMarks(models.Model):
    student_id = models.ForeignKey(StudentID, related_name='student_marks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student_id.student_id} {self.subject.subject_name} {self.marks}"
    
    class Meta:
        unique_together = ['student_id', 'subject']



@receiver(post_save, sender = Student)
def student_added(sender, instance, **kwargs):
    print("################################successfully added################################")
    print(sender, instance, kwargs)