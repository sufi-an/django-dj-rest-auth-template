
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from .models import *

class CustomRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        #user.gender = self.data.get('gender')
        #user.phone_number = self.data.get('phone_number')
        user.save()
        return user



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            'position',
            
            
        )
        read_only_fields = ('id', 'email', 'role')