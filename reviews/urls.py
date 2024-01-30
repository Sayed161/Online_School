from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import ReviewView
router = DefaultRouter()
router.register('review',ReviewView)


urlpatterns = [
    path('',include(router.urls)),
]