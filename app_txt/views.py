from django.shortcuts import redirect, render

from .forms import UserLogin
from .models import User

# Create your views here.


def home(request):
    return render(request, 'intro/home.html')


def register(request):
    form_login = UserLogin()
    context = {
        'form': form_login
    }
    return render(request, 'intro/register.html', context=context)


def login(request):  # A pagina register primeiro tem a funcionalidade e depois renderiza
    new_user = User()
    new_user.username = request.POST.get('usuario')
    new_user.password = request.POST.get('senha')
    new_user.save()
    return render(request, 'intro/data.html')
