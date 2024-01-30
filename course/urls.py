from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import CourseView,CategoryView,LessonView

router = DefaultRouter()
router.register('course',CourseView)
router.register('category',CategoryView)
router.register('lesson',LessonView)
urlpatterns = [
    path('',include(router.urls)),
]