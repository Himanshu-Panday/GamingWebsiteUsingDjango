from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

admin.site.site_header = "This is Admin Himanshu Panday"
admin.site.site_title = "Admin Portal for Himanhu"
admin.site.index_title = "Welcome to the Admin Portal Himanshu Panday"
