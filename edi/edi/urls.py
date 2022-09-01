from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dataExchange/', include('dataExchange.urls')),
    path('admin/', admin.site.urls),
]
