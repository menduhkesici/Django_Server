from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='server'),
    path('homePage', views.home_page, name='server'),
    path('showSystemData', views.system_data, name='system_data'),
    path('fillForm1', views.fillForm1, name='fillForm1'),
    path('fillForm2', views.fillForm2, name='fillForm2'),
    path('button1', views.button1, name='button1'),
    path('button2', views.button2, name='button2'),
    path('button3', views.button3, name='button3'),
    path('resetSystem', views.reset_system, name='reset_system'),
    path('button4', views.button4, name='button4'),
]
