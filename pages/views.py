from django.shortcuts import render
from django.views import generic
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContactUsForm
# Create your views here.


class HomePageView(generic.TemplateView):

    def get_template_names(self):
        if settings.HOME_PAGE in ['home1', 'home2', 'home3']:
            return [f'pages/{settings.HOME_PAGE}.html']
        return ['pages/home1.html']
    

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
    
