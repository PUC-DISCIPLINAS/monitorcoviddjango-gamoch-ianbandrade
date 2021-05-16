from django.contrib import admin

from .models import Covid, Country


class CountryAdmin(admin.ModelAdmin):
  list_display = ("name",)
  ordering = ("name",)


class CovidAdmin(admin.ModelAdmin):
  list_display = ("country", "cases", "deaths", "recovered")
  ordering = ("country",)


admin.site.register(Country, CountryAdmin)
admin.site.register(Covid, CovidAdmin)
