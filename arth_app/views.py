from django.shortcuts import  render ,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm

from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages 
from .models import Utilisateur
from .models import User

'''Chasfat Codes'''
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
             # Rediriger vers la page de connexion après inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigez l'utilisateur vers une page après la connexion
                return redirect('acceuil')  # Change 'home' to the name of your home view
            else:
                 messages.error(request,'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')
def acceuil (request):
     return render(request, 'acceuil.html')
def utilisateurs(request):
    utilisateurs= Utilisateur.objects.all()
    return render(request, 'utilisateurs.html', {'utilisateurs': utilisateurs})
def dashboard (request):
     return render(request, 'dashboard.html')
def utilisateurs (request):
     return render(request, 'utilisateurs.html' , {})
def insertuser(request):
     vuid = request.POST['tuid'];
     vuname = request.POST['tuname'];
     vuprenom = request.POST['tuprenom'];
     vdepartement = request.POST['tdepartement'];
     vuemail = request.POST['tuemail'];
     vtelephone = request.POST['ttelephone'];
     us=User(uid=vuid, uname=vuname, uprenom=vuprenom, departement=vdepartement, uemail=vuemail, telephone=vtelephone );
     us.save();
     return render(request, 'utilisateurs.html', {})

def utilisateurs(request):
     user = User.objects.all()
     return render(request, "utilisateurs.html",{'userdata':user})
 
 
'''
 
 Here is where Chasfat wrote the codes for Authentication and Authorization
'''
def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arth_app:dashboard')
    else:
        form=CustomUserCreationForm()
    return render(request,'arth_app/register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('arth_app:dashboard')
    else:
        form=AuthenticationForm()
    return render(request,'arth_app/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('arth_app:login')

@login_required #Added for authorization purpose 
def dashboard(request):
    return render(request,'arth_app/dashboard.html')
        
        
 
