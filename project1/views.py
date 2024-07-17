from django.shortcuts import render, redirect
from django.http import HttpResponse




def homepage(request):
	return render(request,'index.html')
    # return HttpResponse("hello")


def about(request):
	
	return render(request,'about.html',)
