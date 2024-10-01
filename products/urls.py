from django.urls import path

from . import views

# create your urls here


app_name = 'products'

urlpatterns = [
    path('', views.SearchProductListView.as_view(), name='search_product'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]

