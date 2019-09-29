from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request,"menu.html")
def addmenu(request):
    return render(request,"addmenu.html")