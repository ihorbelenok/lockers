from __future__ import unicode_literals
from rest_framework import serializers
from .models import Locker

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'