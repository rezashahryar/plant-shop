from django.shortcuts import render
from django.views import generic
from django.conf import settings
# Create your views here.


class HomePageView(generic.TemplateView):

    def get_template_names(self):
        if settings.HOME_PAGE in ['home1', 'home2', 'home3']:
            return [f'pages/{settings.HOME_PAGE}.html']
        return ['pages/home1.html']
    

def about_view(request):
    return render(request, 'pages/about.html')
