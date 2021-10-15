from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import mark_safe
from scenario.models.indicator import (
    Indicator, IndicatorGroup, IndicatorFrequency,
    IndicatorValue, IndicatorScenarioRule
)
from scenario.models.harvester import Harvester


class IndicatorScenarioRuleInline(admin.TabularInline):
    model = IndicatorScenarioRule
    extra = 0


class IndicatorValueAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'date', 'geometry', 'value')
    list_filter = ('indicator', 'date', 'geometry')
    search_fields = ('indicator',)


class IndicatorFrequencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency')


class IndicatorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'group', 'scenario_1', 'scenario_2', 'scenario_3', 'scenario_4',
        'frequency', 'show_in_traffic_light', '_harvester', 'geometry_reporting_level')
    list_editable = ('show_in_traffic_light',)
    inlines = (IndicatorScenarioRuleInline,)
    list_filter = ('group', 'show_in_traffic_light')

    def scenario_1(self, indicator: Indicator):
        if indicator.scenario_level and indicator.scenario_level.level == 1:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return ''

    def scenario_2(self, indicator: Indicator):
        if indicator.scenario_level and indicator.scenario_level.level == 2:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return ''

    def scenario_3(self, indicator: Indicator):
        if indicator.scenario_level and indicator.scenario_level.level == 3:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return ''

    def scenario_4(self, indicator: Indicator):
        if indicator.scenario_level and indicator.scenario_level.level == 4:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return ''

    def _harvester(self, indicator: Indicator):
        try:
            change__url = reverse(
                "admin:scenario_harvester_change",
                args=[indicator.harvester.pk])
            return mark_safe(
                f'<a href="{change__url}">{indicator.harvester.harvester_class}</a>')
        except Harvester.DoesNotExist:
            return mark_safe(
                f'<i><a href="{reverse("admin:scenario_harvester_add")}">Create</a></i>')


admin.site.register(IndicatorGroup, admin.ModelAdmin)
admin.site.register(IndicatorFrequency, IndicatorFrequencyAdmin)
admin.site.register(IndicatorValue, IndicatorValueAdmin)
admin.site.register(Indicator, IndicatorAdmin)
