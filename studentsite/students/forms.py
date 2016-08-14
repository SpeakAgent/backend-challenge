from django.forms import ModelForm, Textarea

from .models import School


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"
        widgets = dict(address=Textarea(attrs=dict(rows=2)))
