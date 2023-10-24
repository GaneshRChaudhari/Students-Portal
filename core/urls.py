"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts import views as accounts_views
from homeapp import views as homeapp_views
from students import views as students_views


urlpatterns = [
    path('', accounts_views.login_user, name="login_user"),
    path('logout/', accounts_views.logout_user, name="logout_user"),
    path('search-user/', accounts_views.search_user, name="search_user"),
    path('register-user/', accounts_views.register_user, name="registration_page"),
    path('home/', homeapp_views.home_page, name="home_page"),
    path('students/', students_views.students, name="students_home_page"),
    path('add-student/', students_views.add_student, name="add_student"),
    path('student-marks/<student_id>/', students_views.get_marks, name="get_marks"),
    path('delete-student/<student_id>/', students_views.delete_student, name="delete_student"),
    path('admin/', admin.site.urls),
]
