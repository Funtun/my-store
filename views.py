from django.shortcuts import render 

def home(request):
    return render(request, "online_store\index.html")
