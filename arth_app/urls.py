from django.contrib import admin
from django.urls import path
from arth_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Chasfat codes 
#Added app_name
app_name='arth_app'
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inscription,name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
     path('acceuil/', views.acceuil, name='acceuil'),
     path('acceuil/utilisateurs.html/', views.utilisateurs, name='utilisateurs'),
     path('acceuil/dashboard.html/', views.dashboard, name='dashboard'),
     path('insertuser/', views.insertuser, name='insertuser'),
    

    #Here is where Chasfat started his codes 
    #Register http://localhost:8000/arth_app/register
    path('register',views.register,name='register'),
    #Register http://localhost:8000/arth_app/login
    path('login/',views.login_view,name='login'),
    #Logout http://localhost:8000/arth_app/logout
    path('logout',views.logout_view,name='logout'),
    #Dashboard http://localhost:8000/arth_app/logout
    path('dashboard',views.dashboard,name='dashboard'),
    
   
]

urlpatterns  += staticfiles_urlpatterns()