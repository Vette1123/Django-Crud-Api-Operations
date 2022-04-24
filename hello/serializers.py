from rest_framework import serializers
from .models import Student,Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
 
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'