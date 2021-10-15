from django.contrib import admin
from scenario.models.program import (
    Program, ProgramIntervention
)


class ProgramInterventionInline(admin.TabularInline):
    model = ProgramIntervention
    extra = 0


class ProgramAdmin(admin.ModelAdmin):
    inlines = (ProgramInterventionInline,)


admin.site.register(Program, ProgramAdmin)
