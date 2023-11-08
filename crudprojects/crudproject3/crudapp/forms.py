from django import forms
from crudapp.models import Office
class OfficeForm(forms.ModelForm):
    class Meta:
        model=Office
        fields='__all__'