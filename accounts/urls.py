from django.urls import  path

from accounts.views import login_user, register_user, logout_user

app_name = 'accounts'

urlpatterns =[
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]