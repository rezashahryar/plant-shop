from django.urls import path
from . import views

# create your urls here

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up')
]

