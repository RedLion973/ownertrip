from django.db import models

class Project(models.Model):
    name = models.CharField(u'Name', max_length=255)
    
    def __unicode__(self):
        return u"%s" % (self.name)
