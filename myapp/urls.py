from django.urls import path

from . import views



from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('company', views.company, name='company'),
    path('employee', views.employee, name='employee'),
    path('addemp', views.addemp, name='addemp'),
    path('addcom', views.addcom, name='addcom'),
    path('eedit', views.eedit, name='eedit'),
    path('logout', views.logout, name='logout'),
    path('addcprocess', views.addcprocess, name='addcprocess'),
    path('addeprocess', views.addeprocess, name='addeprocess'),
    path('cedit', views.cedit, name='cedit'),
    path('editcprocess', views.editcprocess, name='editcprocess'),
    path('delcprocess', views.delcprocess, name='delcprocess'),
    path('editeprocess', views.editeprocess, name='editeprocess'),
    path('deleprocess', views.deleprocess, name='deleprocess'),
    path('register', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
