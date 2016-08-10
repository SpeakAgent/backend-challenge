from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON Serializer for Student model.
    """
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'grade', 'dob')
