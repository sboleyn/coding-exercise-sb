from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet


from .serializers import CountySerializer
from .models import County

class CountyViewSet(ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer