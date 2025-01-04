from django.shortcuts import render

app_name = 'main'
# Create your views here.
def home(request):
    return render(request, 'main/home.html')
