
from django.contrib import admin
from django.urls import path, include #I imported include from path
from arth_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inscription,name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
     path('acceuil/', views.acceuil, name='acceuil'),
     path('acceuil/utilisateurs.html/', views.utilisateurs, name='utilisateurs'),
     path('acceuil/dashboard.html/', views.dashboard, name='dashboard'),
     path('insertuser/', views.insertuser, name='insertuser'),
     
     #Chasfat Codes 
     #https://localhost:8000/arth_app/
     path('arth_app/',include('arth_app.urls')),
     
    
]



urlpatterns  += staticfiles_urlpatterns()