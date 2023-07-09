from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('home', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('action', views.action, name = 'action'),
    path('adventure', views.adventure, name = 'adventure'),
    path('roleplaying', views.roleplaying, name = 'roleplaying'),

]
