from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash = False)
router.register('records', views.RecordViewSet)
router.register('images', views.RecordImageViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]