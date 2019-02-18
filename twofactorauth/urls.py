
from django.contrib import admin
from smsauth.views import register
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smsauth.urls')),
]
