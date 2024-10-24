from django.contrib import admin
from django.urls import path, include  # Certifique-se de importar 'include'
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('register/', include('usuario.urls')),

]
