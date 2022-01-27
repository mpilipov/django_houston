from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import StudiesForm
import datetime
# Create your views here.
def index(request):
    return render(request, 'houston/index.html')


def page(request):
    return render(request, 'houston/page.html')

def portfolio(request):
    info = {'portfolio': Portfolio.objects.all()}
    return render(request, 'houston/portfolio.html', context=info)


def add_study(request):
    error=''
    if request.method == "POST":
        form = StudiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
        else:
            error = 'Форма была неверной'

    form = StudiesForm()
    info = {
        'form':form,
        'error':error
    }
    return render(request, 'houston/add_study.html', context=info)