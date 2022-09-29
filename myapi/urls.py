from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

# from . import views
from .views import CountyViewSet

router = routers.SimpleRouter()
router.register(r'levels-by-county', CountyViewSet)

urlpatterns = [
    path('', include(router.urls))
]