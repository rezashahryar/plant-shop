from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us/', views.about_view, name='about'),
    path('contact-us.html/', views.ContactUsView.as_view(), name='contact-us'),
    path('subscribe-newsletter/', views.subscribe_newsletter_view, name='subscribe_newsletter'),
    path('change-unit-money/<str:unit_money>/', views.change_unit_money, name='change_unit_money'),
]
