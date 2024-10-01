from django.urls import path

from . import views

# create your urls here


app_name = 'products'

urlpatterns = [
    path('', views.SearchProductListView.as_view(), name='search_product'),
    path('by-price/', views.search_by_price_list_view, name='search_by_price'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('tags/<slug:slug>/', views.ProductFilterByTagListView.as_view(), name='product_filter_by_tags'),
    path('cat/<slug:slug>/', views.ProductFilterByCategoryListView.as_view(), name='product_filter_by_category'),
]

