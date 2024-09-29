from django.views import generic

from .models import Product

# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = 'products'
