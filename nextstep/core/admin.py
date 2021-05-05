from django.contrib import admin
from nextstep.core.models import *

@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonMediaType)
class PersonMediaTypeAdmin(admin.ModelAdmin):
    pass


class PersonMediaInline(admin.StackedInline):
    model = PersonMedia
    extra = 1

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'cpf', 'phone', 'company', 'last_update')
    inlines = [
        PersonMediaInline,
    ]


@admin.register(PersonAudit)
class PersonAuditAdmin(admin.ModelAdmin):
    pass
