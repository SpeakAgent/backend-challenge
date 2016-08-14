from students.models import Student

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'DOB', 'grade',)

class StudentsMasterList(serializers.ModelSerializer):
    class Meta:
        StudentSerializer.objects.all()
        #all_students = Student.objects.all()
        #return all_students
