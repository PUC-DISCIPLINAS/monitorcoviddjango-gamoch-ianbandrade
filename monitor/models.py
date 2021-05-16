from django.db import models


class Country(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "countries"


class Covid(models.Model):
  country = models.OneToOneField(Country, on_delete=models.CASCADE)
  cases = models.IntegerField()
  deaths = models.IntegerField()
  recovered = models.IntegerField()

  class Meta:
    verbose_name_plural = "covid"
