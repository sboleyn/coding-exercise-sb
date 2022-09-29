from rest_framework import serializers
from .models import County

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = (
            'county',
            'county_fips',
            'state',
            'county_population',
            'health_service_area_number',
            'health_service_area',
            'health_service_area_population',
            'covid_inpatient_bed_utilization',
            'covid_hospital_admissions_per_100k',
            'covid_cases_per_100k',
            'covid19_community_level',
            'date_updated',
        )
        read_only_fields = fields