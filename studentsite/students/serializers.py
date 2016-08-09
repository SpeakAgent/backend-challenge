from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    dob = serializers.SerializerMethodField('get_date_of_birth')

    class Meta:
        model = Student
        fields = ('first_name', 'last_name',
                  'grade', 'dob')

    def get_date_of_birth(self, obj):
        return obj.date_of_birth
