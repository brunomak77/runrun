from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('calendario/', views.creative_tasks, name='calendario'),
    path('calendario/backlog/', views.creative_backlog, name='backlog'),
    path('calendario/colaboradores/', views.creative_users, name='colaboradores'),
    path('calendario/users/', views.users_tasks, name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
