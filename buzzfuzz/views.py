from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView
from .models import Profile
from .forms import ProfileForm


class BuzzListView(ListView):
    template_name = 'buzzfuzz/index.html'
    model = Profile


class BuzzRedirectView(RedirectView):
    url = reverse_lazy('index')


class BuzzDetailView(DetailView):
    template_name = "buzzfuzz/detail.html"
    model = Profile


class BuzzCreateView(CreateView):
    template_name = "buzzfuzz/create.html"
    form_class = ProfileForm

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(BuzzCreateView, self).form_valid(form)


class BuzzDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('index')


class BuzzUpdateView(UpdateView):
    template_name = "buzzfuzz/update.html"
    model = Profile
    form_class = ProfileForm
