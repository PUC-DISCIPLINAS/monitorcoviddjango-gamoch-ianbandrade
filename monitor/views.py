from django.db.models import F
from django.shortcuts import render

from .models import Covid


def index(request):
  covid_data = list(Covid.objects.values(
    "cases", "deaths", "recovered", countryName=F("country__name"))
  )
  context = {"covid_data": covid_data}
  return render(request, "index.html", context)
