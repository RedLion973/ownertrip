from django.utils import unittest
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.general.models import *
from ownertrip.conceptual_model.models import *
from ownertrip.specs.models import *

class ModuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_moduleA = new(Module, number=1, name='some_name')
        self.instance_of_moduleB = self.instance_of_moduleA
        self.instance_of_moduleB.project = get(Project)
        self.instance_of_moduleC = self.instance_of_moduleA
        self.instance_of_moduleA.save()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_moduleA.project, 'not related to a project')
        self.assertEqual(self.instance_of_moduleA.number, 1)
        self.assertEqual(self.instance_of_moduleA.name, 'some_name')
        self.assertIsNotNone(self.instance_of_moduleA.description, 'module description not set')

    def testUniqueness(self):
        try:
            self.instance_of_moduleB.save()
        except:
            self.assertTrue(False, 'numbers & names are unique whatever the project')
        with self.assertRaises(BadDataError, 'numbers & names are not unique inside a project'):
            self.instance_of_moduleC.save()
    
    def testPrint(self):
        self.assertEqual(self.instance_of_moduleA.print_label(), "M01 - some_name")
        self.instance_of_moduleA.number = 99
        self.instance_of_moduleA.name = 'other_name'
        self.assertEqual(self.instance_of_moduleA.print_label(), "M99 - other_name")
        self.instance_of_moduleA.number = 289
        self.assertEqual(self.instance_of_moduleA.print_label(), "M289 - other_name")
        self.assertEqual(self.instance_of_moduleA.print_index(), "M289")

class FunctionTestCase(unittest.TestCase):
    def setUp(self):
        e1 = get(Entity, fields=5)
        e2 = get(Entity, fields=10)
        self.instance_of_functionalityA = new(Functionality, entities=[e1, e2], outputs='something_out', inputs=7, number=1, name='some_name')
        self.instance_of_functionalityB = self.instance_of_functionalityA
        self.instance_of_functionalityB.module = get(Module)
        self.instance_of_functionalityC = self.instance_of_functionalityA
        self.instance_of_functionalityA.save()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_functionalityA.module, 'not related to a module')
        self.assertEqual(self.instance_of_functionalityA.number, 1)
        self.assertEqual(self.instance_of_functionalityA.name, 'some_name')
        self.assertIsNotNone(self.instance_of_functionalityA.description, 'functionality description not set')
        self.assertEqual(self.instance_of_functionalityA.entities.count(), 2, 'number of entities related to the functionality is different from 2')
        self.assertEqual(self.instance_of_functionalityA.outputs, "something_out", 'functionality outputs is not something_out')
        for input in self.instance_of_functionalityA.inputs:
            self.assertIn(input.entity, self.instance_of_functionalityA.entities)

    def testUniqueness(self):
        try:
            self.instance_of_functionalityB.save()
        except:
            self.assertTrue(False, 'numbers & names are unique whatever the module')
        with self.assertRaises(BadDataError, 'numbers & names are not unique inside a module'):
            self.instance_of_functionalityC.save()

    def testPrint(self):
        self.assertEqual(self.instance_of_functionalityA.print_label(), "F01 - some_name")
        self.instance_of_functionalityA.number = 99
        self.instance_of_functionalityA.name = 'other_name'
        self.instance_of_functionalityA.module.number = '55'
        self.assertEqual(self.instance_of_functionalityA.print_full_label(), "M55 F99 - other_name")
        self.instance_of_functionalityA.number = 8
        self.assertEqual(self.instance_of_functionalityA.print_full_label(), "M55 F08 - other_name")
        self.assertEqual(self.instance_of_functionalityA.print_index(), "M55 F08")

class BusinessRuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_businessruleA = new(BusinessRule)
        self.instance_of_businessruleB = self.instance_of_businessruleA
        self.instance_of_businessruleB.functionality = get(Functionality)
        self.instance_of_businessruleC = self.instance_of_businessruleA
        self.instance_of_businessruleA.save()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_businessruleA.functionality, 'not related to a functionality')
        self.assertIsNotNone(self.instance_of_businessruleA.number, 'business rule number not set')
        self.assertIsNotNone(self.instance_of_businessruleA.description, 'business rule description not set')

    def testUniqueness(self):
        try:
            self.instance_of_businessruleB.save()
        except:
            self.assertTrue(False, 'numbers are unique whatever the functionality')
        with self.assertRaises(BadDataError, 'numbers are not unique inside a functionality'):
            self.instance_of_businessruleC.save()

    def testPrint(self):
        self.instance_of_businessruleA.number = 1
        self.instance_of_businessruleA.functionality.number = '5'
        self.instance_of_businessruleA.functionality.module.number = '2'
        self.assertEqual(self.instance_of_businessruleA.print_label(), "M02 F05 - RG01")
        self.instance_of_businessruleA.number = 25
        self.assertEqual(self.instance_of_businessruleA.print_label(), "M02 F05 - RG25")


class OperatingRuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_operatingruleA = new(OperatingRule)
        self.instance_of_operatingruleB = self.instance_of_operatingruleA
        self.instance_of_operatingruleB.functionality = get(Functionality)
        self.instance_of_operatingruleC = self.instance_of_operatingruleA
        self.instance_of_operatingruleA.save()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_operatingruleA.functionality, 'not related to a functionality')
        self.assertIsNotNone(self.instance_of_operatingruleA.number, 'operating rule number not set')
        self.assertIsNotNone(self.instance_of_operatingruleA.description, 'operating rule description not set')

    def testUniqueness(self):
        try:
            self.instance_of_operatingruleB.save()
        except:
            self.assertTrue(False, 'numbers are unique whatever the functionality')
        with self.assertRaises(BadDataError, 'numbers are not unique inside a functionality'):
            self.instance_of_operatingruleC.save()

    def testPrint(self):
        self.instance_of_operatingruleA.number = 1
        self.instance_of_operatingruleA.functionality.number = '5'
        self.instance_of_operatingruleA.functionality.module.number = '2'
        self.assertEqual(self.instance_of_operatingruleA.print_label(), "M02 F05 - RF01")
        self.instance_of_operatingruleA.number = 25
        self.assertEqual(self.instance_of_operatingruleA.print_label(), "M02 F05 - RF25")
