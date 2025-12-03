from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Organization, UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model - basic user info"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for Organization model"""
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'slug', 'description', 'created_at', 'updated_at', 'member_count']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']
    
    def get_member_count(self, obj):
        return obj.members.count()


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model"""
    user = UserSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(),
        source='organization',
        write_only=True
    )
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'organization', 'organization_id', 'role', 'joined_at']
        read_only_fields = ['id', 'joined_at']


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model with organization context"""
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    
    # Write-only fields for assignments
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True,
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'completed',
            'created_at', 'updated_at',
            'organization', 'created_by', 'assigned_to', 'assigned_to_id'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by', 'organization']


