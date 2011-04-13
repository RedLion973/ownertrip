from django.conf.urls.defaults import *
from django.views.generic import ListView
from ownertrip.general.models import *

urlpatterns = patterns('',
    (r'^$', ListView.as_view(model=Project, context_object_name='project_list',)),
)

