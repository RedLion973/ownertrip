from django.utils import unittest
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.conceptual_model.models import *

class TypeTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_type1 = get(Type)
        self.instance_of_type2 = get(Type)

    def testCreation(self):
        self.assertEqual(Type.__unicode__(self.instance_of_type1), "%s" % (self.instance_of_type1.description))
    
    def testDescriptionUniqueness(self):
        self.assertNotEqual(self.instance_of_type1.description, self.instance_of_type2.description)
        with self.assertRaises(BadDataError):
            self.instance_of_type3 = get(Type, description=self.instance_of_type1.description)

class EntityFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_entityfield = get(EntityField)
        type = get(Type)
        self.instance_of_otherentityfield = get(EntityField, type=type, size=11)

    def testCreation(self):
        self.assertIsNotNone(self.instance_of_entityfield.name)
        self.assertIsNotNone(self.instance_of_entityfield.type)
        self.assertTrue(self.instance_of_entityfield.size > 0)

    def testUnicode(self):
        self.assertEqual(EntityField.__unicode__(self.instance_of_otherentityfield), "%s %s(%d) | %s" % (self.instance_of_otherentityfield.name, unicode(self.instance_of_otherentityfield.type).upper(), self.instance_of_otherentityfield.size, self.instance_of_otherentityfield.print_is_null()))

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_otherentity = get(Entity)
        self.instance_of_entity = get(Entity, related_entities=[F(), F(), self.instance_of_otherentity, F()])

    def testCreation(self):
        self.assertIsNotNone(self.instance_of_entity.project)
        self.assertEqual(Entity.__unicode__(self.instance_of_entity), "%s | %s" % (unicode(self.instance_of_entity.project), self.instance_of_entity.name))

    def testRelationship(self):
        self.assertEqual(len(self.instance_of_entity.related_entities.all()), 4)
        self.assertEqual(len(self.instance_of_otherentity.related_entities.all()), 1)
