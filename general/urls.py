from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from ownertrip.general.models import *

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Project, context_object_name='project_list',), name="project-list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Project, context_object_name='project',), name="project-detail"),
)

