from django.contrib import admin
from ownertrip.specs.models import *

class BusinessRuleInline(admin.TabularInline):
    model = BusinessRule
    extra = 3

class OperatingRuleInline(admin.TabularInline):
    model = OperatingRule
    extra = 3

class FunctionalityAdmin(admin.ModelAdmin):
    inlines = [BusinessRuleInline, OperatingRuleInline]

admin.site.register(Module)
admin.site.register(Functionality, FunctionalityAdmin)
