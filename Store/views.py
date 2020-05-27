from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import LoginForm


def main(request):
    context = {"main_page": "active"}
    return render(request, 'main.html', context)


def services(request):
    context = {"services_page": "active"}
    return render(request, 'services.html', context)


def products(request):
    context = {"products_page": "active"}
    return render(request, 'products.html', context)


def cart(request):
    context = {"cart_page": "active"}
    return render(request, 'cart.html', context)

@login_required
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    return render(request, "main.html")
