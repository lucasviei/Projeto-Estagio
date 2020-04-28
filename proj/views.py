from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Acervo

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
     return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente')
    return redirect('/login/')

@login_required(login_url='/login/')
def list_all_obras(request):
    acervo = Acervo.objects.filter(active=True)
    return render(request, 'home.html', {'acervo' :acervo})

def list_user_obras(request):
    acervo = Acervo.objects.filter(active=True,user=request.user)
    return render(request, 'home.html',{'acervo' :acervo})

def obra_detail(request, id):
    acervo = Acervo.objects.get(active=True, id=id)
    return render(request,'obra.html',{'acervo' :acervo})

@login_required(login_url='/login/')
def register_obra(request):
    acervo_id = request.GET.get('id')
    if acervo_id:
        acervo = Acervo.objects.get(id=acervo_id)
        if acervo.user == request.user:
            return render(request, 'register-obra.html', {'acervo':acervo})
    return render(request, 'register-obra.html')


@login_required(login_url='/login/')
def set_obra(request):
    tipoObra = request.POST.get('tipoObra')
    tituloObra = request.POST.get('tituloObra')
    description = request.POST.get('description')
    acervo_id = request.POST.get('acervo-id')
    user = request.user
    if acervo_id:
        acervo = Acervo.objects.get(id=acervo_id)
        if user == acervo.user:
            acervo.tipoObra = tipoObra
            acervo.tituloObra = tituloObra
            acervo.description = description
            acervo.save()
    else:
        acervo = Acervo.objects.create(tipoObra=tipoObra,tituloObra=tituloObra,description=description, user=user)

    url = '/obra/detail/{}/'.format(acervo.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_obra(request, id):
    acervo = Acervo.objects.get(id=id)
    if acervo.user == request.user:
        acervo.delete()
    return redirect('/')