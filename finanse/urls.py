from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finans.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ścieżka do wylogowania
    path('accounts/', include('django.contrib.auth.urls')),  # Logowanie i wylogowanie
]
