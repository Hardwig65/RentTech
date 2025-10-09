from django.urls import path
from authentication.views import logout_view, login_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name = 'logout'),
]