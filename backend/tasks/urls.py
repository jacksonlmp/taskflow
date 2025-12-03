from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, OrganizationViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'organizations', OrganizationViewSet, basename='organization')
router.register(r'profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
]

