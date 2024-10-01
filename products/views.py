from django.shortcuts import render
from django.views import generic
from django.db.models import Count

from .models import CategoryProduct, Product, TagProduct
from .forms import SearchByPriceProductForm

# Create your views here.


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryProduct.objects.all() \
            .annotate(product_count=Count('products'))
        context['tags'] = TagProduct.objects.all()
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        slug = self.kwargs['slug']
        return Product.objects.prefetch_related('images').get(slug=slug)
    

class ProductFilterByCategoryListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryProduct.objects.annotate(product_count=Count('products')).all()
        context['tags'] = TagProduct.objects.all()

        return context
    

class ProductFilterByTagListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(tags__slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryProduct.objects.annotate(product_count=Count('products')).all()
        context['tags'] = TagProduct.objects.all()

        return context
    

class SearchProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        query_search_param = self.request.GET.get('search')
        return Product.objects.filter(title__icontains=query_search_param)


def search_by_price_list_view(request):
    form = SearchByPriceProductForm(request.GET)
    context = {}
    if form.is_valid():
        price1 = form.cleaned_data['price1']
        price2 = form.cleaned_data['price2']
        context['products'] = Product.objects.filter(unit_price__gt=price1, unit_price__lt=price2)
    context['categories'] = CategoryProduct.objects.all() \
            .annotate(product_count=Count('products'))
    context['tags'] = TagProduct.objects.all()

    return render(request, 'products/product_list.html', context)
