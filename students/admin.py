from django.contrib import admin

# Register your models here.
from students.models import *


admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)

class SubjectMarksDisplay(admin.ModelAdmin):
    list_display = ['student_id', 'subject', 'marks']

admin.site.register(SubjectMarks)
