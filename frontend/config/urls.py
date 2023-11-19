from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', include('authentication.urls')),
    path('rest_api/', include('rest_api.urls')),
    path('admin/', admin.site.urls),
]
