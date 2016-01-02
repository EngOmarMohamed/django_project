from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request, id = 0):
	if id == 0:
		return HttpResponse("you haven't enter ID in URL")
	else :
		student = Student.objects.all()
		context = {'student': student}
		return render(request, 'students/index.html', context)