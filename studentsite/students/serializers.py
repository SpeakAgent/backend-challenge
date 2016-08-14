from model import Student

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'DOB', 'grade',)
