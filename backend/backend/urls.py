from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    # path('', include('apps.form.urls')),
]
