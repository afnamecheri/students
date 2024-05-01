# serializers.py
from rest_framework import serializers
from .models import Department, Students

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    department = serializers.CharField()

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        department_name = validated_data.pop('department', None)
        validated_data['department'] = department_name
        return super().create(validated_data)
