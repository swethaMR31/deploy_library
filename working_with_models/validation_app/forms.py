from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Enter a name starting with z/Z")

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Confirm your Email: ")
    text = forms.CharField(widget = forms.Textarea)
    #botcatcher = forms.CharField(required = False, widget = forms.HiddenInput) #used for inbuilt validation method
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)]) #used for  validation method

    """def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("We Got U Bot!")
        return botcatcher"""

    def clean(self):    #cleaning the whole form
        all_clean_data = super().clean
        email = self.cleaned_data["email"]
        vemail =self.cleaned_data["verify_email"]

        if email != vemail:
            raise forms.ValidationError("Enter correct Email")