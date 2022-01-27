from django.shortcuts import render

# Create your views here.
def piedpaper(request):
    return render(request, 'piedpaper/piedpaper.html')