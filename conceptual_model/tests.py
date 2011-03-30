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
        self.instance_of_entityA = new(Entity, description='some_description', fields=5)
        self.instance_of_entityB = self.instance_of_entityA
        self.instance_of_entityB.project = get(Project)
        self.instance_of_entityC = self.instance_of_entityA
        self.instance_of_entityA.save()
        self.instance_of_entityD = get(Entity, related_entities=[F(), F(), self.instance_of_entityA])

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_entityA.project, 'not related to a project')
        self.assertIsNotNone(self.instance_of_entityA.name, (entity name is not set')
        self.assertEqual(self.instance_of_entityA.description, 'some_description')
        self.assertEqual(self.instance_of_entityA.related_entities.count(), 1)
        self.assertEqual(self.instance_of_entityD.related_entities.count(), 3)
        self.assertEqual(self.instance_of_entityD.fields.count(), 5)

    def testUniqueness(self):
        try:
            self.instance_of_entityB.save()
        except:
            self.assertTrue(False, 'names are unique whatever the project')
        with self.assertRaises(BadDataError, 'names are not unique inside a project'):
            self.instance_of_entityC.save()

    def testPrint(self):
        self.instance_of_entity.name = 'entity'
        self.assertEqual(Entity.__unicode__(self.instance_of_entity), "entity")
