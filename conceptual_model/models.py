from django.db import models
from ownertrip.general.models import Project

class Entity(models.Model):
    project = models.ForeignKey(Project, verbose_name=u'Project', related_name='entities')
    name = models.CharField(u'Name', max_length=255)
    related_entities = models.ManyToManyField('self', verbose_name=u'Related Entities', blank=True, null=True)
    
    def __unicode__(self):
        return u"%s | %s" % (unicode(self.project), self.name)
    
    class Meta:
        verbose_name, verbose_name_plural = (u'Entity',u'Entities')

class Type(models.Model):
    description = models.CharField(u'Description', max_length=255, unique=True)
    
    def __unicode__(self):
        return u"%s" % (self.description)

class EntityField(models.Model):
    entity = models.ForeignKey(Entity, verbose_name=u'Entity')
    name = models.CharField(u'Name', max_length=255)
    type = models.ForeignKey(Type, verbose_name=u'Type')
    size = models.PositiveIntegerField(u'Size')
    null = models.BooleanField(u'Null', default=0)

    def print_is_null(self):
        if 0 == self.null:
            return "not null"
        else:
            return "null"

    def __unicode__(self):
        return u"%s %s(%d) | %s" % (self.name, unicode(self.type).upper(), self.size, self.print_is_null())

