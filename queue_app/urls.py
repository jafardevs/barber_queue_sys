from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.queue_list_view, name='queue_list'),
    path('finish/<int:customer_id>/', views.finish_customer_view, name='finish_customer'),

    # Barber Authentication
    path(
        'barber/login/',
        auth_views.LoginView.as_view(template_name='queue_app/login.html'),
        name='barber_login',
    ),
    path(
        'barber/logout/',
        auth_views.LogoutView.as_view(next_page='queue_list'),
        name='barber_logout',
    ),
]
