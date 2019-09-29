from django.shortcuts import render

# Create your views here.
def articlelist(request):
    return render(request,"articlelist.html")
def addarticle(request):
    return render(request,"addarticle.html")