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

class Functionality(models.Model):
    module = models.ForeignKey(Module, verbose_name=u'Module', related_name='modules')
    number = models.PositiveIntegerField(u'Number')
    name = models.CharField(u'Name', max_length=255)
    description = models.TextField(u'Description')
    inputs = models.ManyToManyField(EntityField, verbose_name=u'Inputs')
    outputs = models.TextField(u'Outputs', blank=True)

    def __unicode__(self):
        return u"%s" % (self.name)

    def print_label(self):
        if self.number < 10 :
            return u"F%s - %s" % (str(self.number).zfill(2), self.name)
        else:
            return u"F%s - %s" % (str(self.number), self.name)         

    def print_full_label(self):
        if self.number < 10 :
            return u"%s F%s - %s" % (self.module.print_index(), str(self.number).zfill(2), self.name)
        else:
            return u"%s F%s - %s" % (self.module.print_index(), str(self.number), self.name)

    def print_index(self):
        if self.number < 10 :
            return u"%s F%s" % (self.module.print_index(), str(self.number).zfill(2))
        else:
            return u"%s F%s" % (self.module.print_index(), str(self.number))

    class Meta:
        verbose_name, verbose_name_plural = (u'Functionality', u'Functionalities')
        unique_together = ("module", "number", "name")

class BusinessRule(models.Model):
    functionality = models.ForeignKey(Functionality, verbose_name=u'Functionality', related_name='business_rules')
    number = models.PositiveIntegerField(u'Number')
    description = models.TextField(u'Description')

    def __unicode__(self):
        return u"%s" % (self.print_label())

    def print_label(self):
        if self.number < 10 :
            return u"%s - RG%s" % (self.functionality.print_index(), str(self.number).zfill(2))
        else:
            return u"%s - RG%s" % (self.functionality.print_index(), str(self.number))

    class Meta:
        verbose_name, verbose_name_plural = (u'Business Rule', u'Business Rules')
        unique_together = ("functionality", "number")

class OperatingRule(models.Model):
    functionality = models.ForeignKey(Functionality, verbose_name=u'Functionality', related_name='operating_rules')
    number = models.PositiveIntegerField(u'Number')
    description = models.TextField(u'Description')

    def __unicode__(self):
        return u"%s" % (self.print_label())

    def print_label(self):
        if self.number < 10 :
            return u"%s - RG%s" % (self.functionality.print_index(), str(self.number).zfill(2))
        else:
            return u"%s - RG%s" % (self.functionality.print_index(), str(self.number))

    class Meta:
        verbose_name, verbose_name_plural = (u'Operating Rule', u'Operating Rules')
        unique_together = ("functionality", "number")
