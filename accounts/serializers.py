from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        # user.set_password(validated_data['password'])
        # user.save()
        return user
    
class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    '''
    serializer for password change endpoint
    '''
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    