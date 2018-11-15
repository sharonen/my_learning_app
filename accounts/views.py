from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignIn(generic.CreateView):
    from_class = UserCreationForm
    model = User
    success_url = reverse_lazy("random_links:detail")
    template_name = 'accounts/signin.html'


