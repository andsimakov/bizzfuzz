from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView, View

from .models import Profile, User
from .forms import ProfileForm
from django.http import HttpResponse
import csv


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
    template_name = "buzzfuzz/edit.html"
    model = Profile
    form_class = ProfileForm


class ExportProfilesView(ListView):
    """
    The standard view for HTML return
    """
    template_name = 'buzzfuzz/index.html'
    model = Profile
    context_object_name = 'profile_list'

    def get_queryset(self):
        return Profile.objects.all


class ExportProfilesCsvView(ExportProfilesView):
    """
    Subclass of previous view, to export a CSV file
    """
    template_name = 'buzzfuzz/profilelist.csv'
    content_type = 'text/csv'


