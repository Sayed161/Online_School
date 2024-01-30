from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import StudentView,EnrollView,UserRegistration,UserLoginView,User_logout_view

router = DefaultRouter()
router.register('student',StudentView)
router.register('enroll',EnrollView)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',User_logout_view.as_view(),name='logout'),
]