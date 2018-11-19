from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic

from . import forms
from . import models



def random_link_detail(request):
    return render(request, 'random_links/random_links_detail.html')


class RandomLinksListView(LoginRequiredMixin, generic.ListView ):
    context_object_name = "links"
    model= models.Random_Link
    template_name = "random_links/random_links_list.html"
    login_url = 'accounts:login'
    
    def get_queryset(self):
        try:
            self.save_user = User.objects.prefetch_related("random_links").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.save_user.random_links.all()
    
    

    
class RandomLinksCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.SaveForm
    model = models.Random_Link
    login_url = "accounts:login"
    
    def get_form_kwargs(self):
        kwargs = super(RandomLinksCreateView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        try:
            self.object.save()
            return super(RandomLinksCreateView, self).form_valid(form)
        except IntegrityError:
            return render(self.request, 'random_links/random_links_was_saved.html')
        
   

    
class RandonLinksDeleteView(LoginRequiredMixin, generic.DeleteView):
    context_object_name = "link"
    model = models.Random_Link
    login_url = "accounts:login"
    
    def get_queryset(self):
        queryset = super(RandonLinksDeleteView, self).get_queryset()
        return queryset.filter(user_id=self.request.user.id)
    
    
    def get_success_url(self):
       return reverse_lazy('random_links:list',
                            kwargs={'username': self.request.user.username})
    
    
    