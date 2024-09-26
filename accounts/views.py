from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationForm
# Create your views here.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('pages:home')
