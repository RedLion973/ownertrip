from django.utils import unittest
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.general.models import *
from ownertrip.conceptual_model.models import Entity

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_project = get(Project)
        a = get(Entity, project=self.instance_of_project)
        b = get(Entity, project=self.instance_of_project)
        c = get(Entity, project=self.instance_of_project)
        d = get(Entity, project=self.instance_of_project)

    def testCreation(self):
        self.assertEqual(Project.__unicode__(self.instance_of_project), "%s" % (self.instance_of_project.name))

    def testRelationship(self):
        self.assertEqual(self.instance_of_project.entities.count(), 4)
