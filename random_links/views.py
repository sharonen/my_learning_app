from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import(
     ListView, DetailView,
     CreateView, DeleteView
     )

from braces.views import SelectRelatedMixin


from . import models



def random_link_detail(request):
    # TODO: check if user is login
    return render(request, 'random_links/random_links_detail.html')



class RandomLinksListView(LoginRequiredMixin, ListView ):
    context_object_name = "links"
    model= models.Random_Link
    template_name = "random_links/random_links_list.html"
    login_url = 'login'


class RandomLinksDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "link"
    model = models.Random_Link
    template_name = "random_links/random_links_detail.html"
    login_url = 'login'
    
class RandomLinksCreateView(LoginRequiredMixin, CreateView):
    fields = ("title","url")
    model = models.Random_Link
    page_title = "Save the link"
    login_url = 'login'
    
    
class RandonLinksDeleteView(LoginRequiredMixin, DeleteView):
    context_object_name = "link"
    model = models.Random_Link
    success_url = reverse_lazy("random_links:list")
    login_url = 'login'
    
   # def get_queryset(self):
    #    owner = self.request.user
     #   return self.model.objects.filter(owner=owner)
    