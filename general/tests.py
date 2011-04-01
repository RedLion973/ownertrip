from django.utils import unittest
from django.db import IntegrityError
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.general.models import *
from ownertrip.conceptual_model.models import Entity

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_project = get(Project, name="some_project")

    def tearDown(self):
        Project.objects.get(pk=self.instance_of_project.pk).delete()

    def testFieldsAndRelationships(self):
        A = get(Entity, project=self.instance_of_project)
        B = get(Entity, project=self.instance_of_project)
        C = get(Entity, project=self.instance_of_project)
        D = get(Entity, project=self.instance_of_project)
        self.assertEqual(self.instance_of_project.name, "some_project")
        self.assertEqual(self.instance_of_project.entities.count(), 4)
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            p = get(Project, name=None)

    def testUniqueness(self):
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            p = get(Project, name="some_project")

    def testPrint(self):
        self.assertEqual(Project.__unicode__(self.instance_of_project), "some_project")
