from django.utils import unittest
from django_dynamic_fixture import new, get, DynamicFixture as F, print_field_values, BadDataError
from ownertrip.general.models import *
from ownertrip.conceptual_model.models import *
from ownertrip.specs.models import *

class ModuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_module = get(Module, number=1, name='some_name')

    def tearDown(self):
        Module.objects.get(pk=self.instance_of_module.pk).delete()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_module.project, 'not related to a project')
        self.assertEqual(self.instance_of_module.number, 1)
        self.assertEqual(self.instance_of_module.name, 'some_name')
        self.assertIsNotNone(self.instance_of_module.description, 'module description not set')

    def testUniqueness(self):
        try:
            M = get(Module, number=1, name='some_name')
        except:
            self.assertTrue(False, 'number & name are unique whatever the project')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            M = get(Module, number=1, name='some_name', project=self.instance_of_module.project)
    
    def testPrint(self):
        self.assertEqual(Module.__unicode__(self.instance_of_module), "some_name")
        self.assertEqual(self.instance_of_module.print_label(), "M01 - some_name")
        self.instance_of_module.number = 99
        self.instance_of_module.name = 'other_name'
        self.assertEqual(self.instance_of_module.print_label(), "M99 - other_name")
        self.instance_of_module.number = 289
        self.assertEqual(self.instance_of_module.print_label(), "M289 - other_name")
        self.assertEqual(self.instance_of_module.print_index(), "M289")

class FunctionalityTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_functionality = get(Functionality, outputs='something_out', inputs=7, number=1, name='some_name')

    def tearDown(self):
        Functionality.objects.get(pk=self.instance_of_functionality.pk).delete()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_functionality.module, 'not related to a module')
        self.assertEqual(self.instance_of_functionality.number, 1)
        self.assertEqual(self.instance_of_functionality.name, 'some_name')
        self.assertIsNotNone(self.instance_of_functionality.description, 'functionality description not set')
        self.assertEqual(self.instance_of_functionality.outputs, "something_out", 'functionality outputs is not something_out')
        self.assertEqual(self.instance_of_functionality.inputs.count(), 7, 'number of inputs to the functionality is different from 7')

    def testUniqueness(self):
        try:
            F = get(Functionality, number=1, name='some_name')
        except:
            self.assertTrue(False, 'number & name are unique whatever the module')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            F = get(Functionality, number=1, name='some_name', module=self.instance_of_functionality.module)

    def testPrint(self):
        self.assertEqual(Functionality.__unicode__(self.instance_of_functionality), "some_name")
        self.assertEqual(self.instance_of_functionality.print_label(), "F01 - some_name")
        self.instance_of_functionality.number = 99
        self.instance_of_functionality.name = 'other_name'
        self.instance_of_functionality.module.number = '55'
        self.assertEqual(self.instance_of_functionality.print_full_label(), "M55 F99 - other_name")
        self.instance_of_functionality.number = 8
        self.assertEqual(self.instance_of_functionality.print_full_label(), "M55 F08 - other_name")
        self.assertEqual(self.instance_of_functionality.print_index(), "M55 F08")

class BusinessRuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_businessrule = get(BusinessRule, number=1, functionality=F(module=F(project=F()), insputs=3))

    def tearDown(self):
        BusinessRule.objects.get(pk=self.instance_of_businessrule.pk).delete()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_businessrule.functionality, 'not related to a functionality')
        self.assertIsNotNone(self.instance_of_businessrule.number, 'business rule number not set')
        self.assertEqual(self.instance_of_businessrule.number, 1)
        self.assertIsNotNone(self.instance_of_businessrule.description, 'business rule description not set')

    def testUniqueness(self):
        try:
            B = get(BusinessRule, number=1)
        except:
            self.assertTrue(False, 'number is unique whatever the functionality')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            B = get(BusinessRule, number=1, functionality=self.instance_of_businessrule.functionality)

    def testPrint(self):
        self.instance_of_businessrule.functionality.number = 5
        self.instance_of_businessrule.functionality.module.number = 2
        self.assertEqual(self.instance_of_businessrule.print_label(), "M02 F05 - RG01")
        self.assertEqual(BusinessRule.__unicode__(self.instance_of_businessrule), "M02 F05 - RG01")
        self.instance_of_businessrule.number = 25
        self.assertEqual(self.instance_of_businessrule.print_label(), "M02 F05 - RG25")


class OperatingRuleTestCase(unittest.TestCase):
    def setUp(self):
        self.instance_of_operatingrule = get(OperatingRule, number=1, functionality=F(module=F(project=F()), insputs=3))

    def tearDown(self):
        OperatingRule.objects.get(pk=self.instance_of_operatingrule.pk).delete()

    def testFieldsAndRelationships(self):
        self.assertIsNotNone(self.instance_of_operatingrule.functionality, 'not related to a functionality')
        self.assertIsNotNone(self.instance_of_operatingrule.number, 'operating rule number not set')
        self.assertEqual(self.instance_of_operatingrule.number, 1)
        self.assertIsNotNone(self.instance_of_operatingrule.description, 'operating rule description not set')

    def testUniqueness(self):
        try:
            B = get(OperatingRule, number=1)
        except:
            self.assertTrue(False, 'number is unique whatever the functionality')
        with self.assertRaises(BadDataError) or self.assertRaises(IntegrityError):
            B = get(OperatingRule, number=1, functionality=self.instance_of_operatingrule.functionality)

    def testPrint(self):
        self.instance_of_operatingrule.functionality.number = 5
        self.instance_of_operatingrule.functionality.module.number = 2
        self.assertEqual(self.instance_of_operatingrule.print_label(), "M02 F05 - RG01")
        self.assertEqual(OperatingRule.__unicode__(self.instance_of_operatingrule), "M02 F05 - RG01")
        self.instance_of_operatingrule.number = 25
        self.assertEqual(self.instance_of_operatingrule.print_label(), "M02 F05 - RG25")

