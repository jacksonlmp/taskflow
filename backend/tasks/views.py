from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Task, Organization, UserProfile
from .serializers import TaskSerializer, OrganizationSerializer, UserProfileSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Organization CRUD operations
    """
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return organizations where the user is a member"""
        return Organization.objects.filter(
            members__user=self.request.user
        ).distinct()
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get all members of an organization"""
        organization = self.get_object()
        profiles = UserProfile.objects.filter(organization=organization)
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get the user's current/default organization"""
        try:
            profile = UserProfile.objects.filter(
                user=request.user
            ).order_by('-role').first()
            
            if profile:
                serializer = OrganizationSerializer(profile.organization)
                return Response(serializer.data)
            return Response(
                {'detail': 'No organization found for user'},
                status=status.HTTP_404_NOT_FOUND
            )
        except UserProfile.DoesNotExist:
            return Response(
                {'detail': 'No organization found for user'},
                status=status.HTTP_404_NOT_FOUND
            )


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for UserProfile CRUD operations
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return profiles for organizations the user belongs to"""
        user_orgs = Organization.objects.filter(members__user=self.request.user)
        return UserProfile.objects.filter(organization__in=user_orgs)


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task CRUD operations with organization filtering
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Return tasks for the user's organizations
        Filter by organization, created_by, or assigned_to
        """
        user = self.request.user
        user_orgs = Organization.objects.filter(members__user=user)
        
        # Return tasks from user's organizations or tasks created by/assigned to the user
        return Task.objects.filter(
            Q(organization__in=user_orgs) |
            Q(created_by=user) |
            Q(assigned_to=user)
        ).distinct().order_by('-created_at')
    
    def perform_create(self, serializer):
        """
        Auto-assign the creator and their default organization on task creation
        """
        user = self.request.user
        
        # Get user's primary organization (owner role preferred)
        try:
            profile = UserProfile.objects.filter(
                user=user
            ).order_by('-role').first()
            
            organization = profile.organization if profile else None
        except UserProfile.DoesNotExist:
            organization = None
        
        serializer.save(
            created_by=user,
            organization=organization
        )


