from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects #get all of the Job objects and store in jobs variable
    return render(request, 'jobs/home.html', { 'jobs1':jobs })
