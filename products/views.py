from django.views import generic

from .models import Product

# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        slug = self.kwargs['slug']
        return Product.objects.prefetch_related('images').get(slug=slug)
