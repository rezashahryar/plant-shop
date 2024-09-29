from django.urls import path

from . import views

# create your urls here


app_name = 'products'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
]

