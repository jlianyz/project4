from django.urls import path
from .views import logout, login, register, update_details

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('update/', update_details, name='update'),
]
