from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'email', 'password', 'national_code', 'first_name', 'last_name', 'is_superuser', 'user_permissions']