from django.contrib import admin
from ownertrip.conceptual_model.models import *

class EntityFieldInline(admin.StackedInline):
    model = EntityField
    extra = 5

class EntityAdmin(admin.ModelAdmin):
    inlines = [EntityFieldInline]

admin.site.register(Type)
admin.site.register(Entity, EntityAdmin)
