from django.db import models
from ownertrip.general.models import *
from ownertrip.conceptual_model.models import *

class Module(models.Model):
    project = models.ForeignKey(Project, verbose_name=u'Project', related_name='modules')
    number = models.PositiveIntegerField(u'Number')
    name = models.CharField(u'Name', max_length=255)
    description = models.TextField(u'Description')
    
    def __unicode__(self):
        return u"%s" % (self.name)

    def print_label(self):
        if self.number < 10 :
            return u"M%s - %s" % (str(self.number).zfill(2), self.name) 
        else:
            return u"M%s - %s" % (str(self.number), self.name) 

    def print_index(self):
        if self.number < 10 :
            return u"M%s" % (str(self.number).zfill(2))
        else:
            return u"M%s" % (str(self.number))

    class Meta:
        unique_together = ("project", "number", "name")
