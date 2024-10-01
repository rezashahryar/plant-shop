from django.shortcuts import redirect, render
from django.views import generic
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.models import Product

from .forms import ContactUsForm, SubscribeNewsLetterForm
# Create your views here.


class HomePageView(generic.TemplateView):

    def get_template_names(self):
        if settings.HOME_PAGE in ['home1', 'home2', 'home3']:
            return [f'pages/{settings.HOME_PAGE}.html']
        return ['pages/home1.html']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:10]

        return context
    

def about_view(request):
    return render(request, 'pages/about.html')


class ContactUsView(generic.FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '.پیغام شما با موفقیت ارسال شد. از همکاری شما سپاسگزاریم')
        return super().form_valid(form)


@require_POST
def subscribe_newsletter_view(request):
    form = SubscribeNewsLetterForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'your email successfully saved, thanks you')
    return redirect('pages:home')
