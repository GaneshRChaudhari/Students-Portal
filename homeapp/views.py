from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/")
def home_page(request):
    return render(request, 'home.html')
