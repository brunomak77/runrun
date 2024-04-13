from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('mainent/', admin.site.urls),
    path('', include('accounts.urls')),
    path('calendario/', include('calendario.urls')),
]
