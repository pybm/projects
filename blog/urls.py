from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('welcome.urls')),
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]
