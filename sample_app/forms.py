from django import forms
from .models import Calc

 
 
 
# creating a form
class CalcForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    # name = forms.CharField(label="項目")
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Calc
 
        # specify fields to be used
        fields = [
            "num1",
            "num2",
        ]

        widgets= {
            "num1" :forms.TextInput(attrs={"placeholder" :"NUM1"}),
            "num2" :forms.TextInput(attrs={"placeholder" :"NUM2"}),
        }