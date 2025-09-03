from django.db import models

# Create your models here.
class CaveSite(models.Model):
  cave_name = models.CharField(max_length=100)
  municity = models.CharField(max_length=100, null=True)
  province = models.CharField(max_length=100, null=True)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)

  def __str__(self):
    return self.cave_name

class IsolationSource(models.Model):
  sampling_type = models.CharField(max_length=100)
  cave_site = models.ForeignKey(CaveSite, on_delete=models.CASCADE, related_name='caves')
  sampling_point = models.IntegerField(null=True)
  sampling_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.id}: {self.cave_site}-{self.sampling_type}"