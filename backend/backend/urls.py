from django.contrib import admin
from django.urls import path, include
from apps.form.admin import admin_site

urlpatterns = [
    path('', admin_site.urls),
    #path('', include('apps.form.urls')),
]
