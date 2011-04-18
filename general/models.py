from django.db import models
from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote

class Project(models.Model):
    name = models.CharField(u'Name', max_length=255, unique=True)
    
    def __unicode__(self):
        return u"%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', (), {'pk': self.pk})
