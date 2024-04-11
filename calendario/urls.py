from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.creative_tasks, name='tarefas'),
    path('backlog/', views.creative_backlog, name='backlog'),
    path('colaboradores/', views.creative_users, name='colaboradores'),
    path('users/', views.users_tasks, name='users'),
    path('teste/', views.teste, name='teste'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
