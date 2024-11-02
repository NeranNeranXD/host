from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Aga
from .forms import AgaForm
# Create your views here.
def index(request):
    error = ''
    if request.method == "POST":
        form = AgaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
        else:
            error = 'Вы где то проебались, проверьте написание формы'

    form = AgaForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/xyi.html')
# да можно сделать шаблонизатор джинджа но нахуй надо я думаю
# это урок 4 у итпрогер 8 минута