from django.conf.urls import url
from . import views
from .views import BuzzListView, BuzzDetailView, BuzzCreateView, BuzzDeleteView, BuzzUpdateView

app_name = 'buzzfuzz'

urlpatterns = [
    url(r'^$', BuzzListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BuzzDetailView.as_view(), name='detail'),
    url(r'^create/$', BuzzCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', BuzzDeleteView.as_view(), name='delete'),
    url(r'^edit/(?P<pk>\d+)/$', BuzzUpdateView.as_view(), name='edit'),
]