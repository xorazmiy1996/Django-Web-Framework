from django.urls import path, include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register_ulr'),
    path('edit-profile/', views.edit_user_profile, name='edit_profile_ulr'),
    path('login/', views.login_view, name='login'),
    path('', include("django.contrib.auth.urls")), # Masalan: 'login/', 'logout/', 'password_change', 'password_reset/' va ..... Bu url standart funksiyalarg olib bradi. Bu funksiyalr Django bilan birga keladi.
]