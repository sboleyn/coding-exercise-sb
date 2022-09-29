from django.db import models

# Create your models here.
class County(models.Model):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    covid19_community_level = [(LOW, 'Low'), (MEDIUM, "Medium"), (HIGH, "High")]

    county = models.CharField(max_length = 50,null = False)
    county_fips = models.IntegerField(null = False)
    state = models.CharField(max_length = 50, null = False)
    county_population = models.IntegerField()
    health_service_area_number = models.IntegerField()
    health_service_area = models.TextField()
    health_service_area_population = models.IntegerField(null = True, blank=True)
    covid_inpatient_bed_utilization = models.DecimalField(max_digits = 3, decimal_places=1, null=True, blank=True)
    covid_hospital_admissions_per_100k = models.DecimalField(max_digits = 7, decimal_places=1, null=True, blank=True)
    covid_cases_per_100k = models.DecimalField(max_digits = 7, decimal_places=2)
    covid19_community_level = models.CharField(max_length = 6, choices = covid19_community_level, null=True)
    date_updated = models.DateField()