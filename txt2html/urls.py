from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('converter.urls')),  # 👈 connects to your app
    path('admin/', admin.site.urls),
]
