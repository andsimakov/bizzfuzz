from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView

from .models import Profile
from .forms import ProfileForm


class BuzzListView(ListView):
    template_name = 'bizzfuzz/index.html'
    model = Profile


class BuzzRedirectView(RedirectView):
    url = reverse_lazy('index')


class BuzzDetailView(DetailView):
    template_name = 'bizzfuzz/detail.html'
    model = Profile


class BuzzCreateView(CreateView):
    template_name = 'bizzfuzz/create.html'
    form_class = ProfileForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BuzzCreateView, self).form_valid(form)


class BuzzDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('bizzfuzz:index')


class BuzzUpdateView(UpdateView):
    template_name = 'bizzfuzz/edit.html'
    model = Profile
    fields = ['birthday']


class ExportProfilesView(ListView):
    """
    The standard view for HTML return
    """
    template_name = 'bizzfuzz/index.html'
    model = Profile
    context_object_name = 'profile_list'

    def get_queryset(self):
        return Profile.objects.all


class ExportProfilesCsvView(ExportProfilesView):
    """
    Subclass of previous view, to export a CSV file
    """
    template_name = 'bizzfuzz/profilelist.csv'
    content_type = 'text/csv'
