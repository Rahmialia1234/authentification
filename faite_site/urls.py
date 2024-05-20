
from django.contrib import admin
from django.urls import path
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
    
]



urlpatterns  += staticfiles_urlpatterns()