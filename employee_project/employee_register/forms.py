from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','emp_code','mobile','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP Code'
        }
    
    # this fucntion is use for the dropdown position adding select field
    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"

