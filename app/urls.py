from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('voting/', views.voting, name='voting'),
    path('logout/', views.user_logout, name='logout'),
    # Add more URLs as needed
]
