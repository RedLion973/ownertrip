from django.utils import unittest
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.conceptual_model.models import *

class TypeTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_type = get(Type, description="some_type")

    def tearDown(self):
        Type.objects.get(pk=self.instance_of_type.pk).delete()

    def testField(self):
        self.assertEqual(self.instance_of_type.description, "some_type")
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            T = get(Type, description=None)

    def testUniqueness(self):
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            T = get(Type, description="some_type")
    
    def testPrint(self):
        self.assertEqual(Type.__unicode__(self.instance_of_type), "some_type")


class EntityFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_field = get(EntityField, name="some_field", size=5, null=0)

    def tearDown(self):
        EntityField.objects.get(pk=self.instance_of_field.pk).delete()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_field.entity, 'not related to an entity')
        self.assertIsNotNone(self.instance_of_field.type, 'field type is not set')
        self.assertIsNotNone(self.instance_of_field.size, 'field size is not set')
        self.assertEqual(self.instance_of_field.name, "some_field")
        self.assertEqual(self.instance_of_field.null, 0)

    def testUniqueness(self):
        try:
            F = get(EntityField, name="some_field")
        except:
            self.assertTrue(False, 'name is unique whatever the entity')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            F = get(EntityField, name="some_field", entity=self.instance_of_field.entity)

    def testPrint(self):
        self.assertEqual(EntityField.__unicode__(self.instance_of_field), "some_field " + unicode(self.instance_of_field.type).upper() + "(5) | not null")

class EntityTestCase(unittest.TestCase):
    def setUp(self):
	self.instance_of_entityA = get(Entity, name="foo", description='some_description')
        self.instance_of_entityB = get(Entity, related_entities=[F(), F(), self.instance_of_entityA])

    def tearDown(self):
        Entity.objects.get(pk=self.instance_of_entityA.pk).delete()
        Entity.objects.get(pk=self.instance_of_entityB.pk).delete()

    def testFieldsAndRelationships(self):
        F1 = get(EntityField, entity=self.instance_of_entityA)
        F2 = get(EntityField, entity=self.instance_of_entityA)
        F3 = get(EntityField, entity=self.instance_of_entityA)
        F4 = get(EntityField, entity=self.instance_of_entityA)
        F5 = get(EntityField, entity=self.instance_of_entityA)
        self.assertIsNotNone(self.instance_of_entityA.project, 'not related to a project')
        self.assertIsNotNone(self.instance_of_entityA.name, 'entity name is not set')
        self.assertEqual(self.instance_of_entityA.description, 'some_description')
        self.assertEqual(self.instance_of_entityA.fields.count(), 5)
        self.assertEqual(self.instance_of_entityA.related_entities.count(), 1)
        self.assertEqual(self.instance_of_entityB.related_entities.count(), 3)

    def testUniqueness(self):
        try:
            E = get(Entity, name="foo", description='some_description', fields=5)
        except:
            self.assertTrue(False, 'name is unique whatever the project')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            E = get(Entity, name="foo", description='some_description', fields=5, project=self.instance_of_entityA.project)

    def testPrint(self):
        self.assertEqual(Entity.__unicode__(self.instance_of_entityA), "foo")
