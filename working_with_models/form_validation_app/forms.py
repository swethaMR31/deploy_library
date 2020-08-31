from django import forms
from django.core import validators
import re

from django.core.validators import URLValidator


def validate_phone(value):
    mobile = str(value)
    pattern = re.compile("[6-9][0-9]{9}")
    if not(pattern.match(mobile)):
        raise forms.ValidationError("Enter a valid phone number")

def validate_aadhar(aadhar):
    pattern = re.compile("^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$")
    if not(pattern.match(aadhar)):
        raise forms.ValidationError("Enter a valid aadhar number")

'''def validate_url(value):
    url = value
    pattern = re.compile("(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
    #   ^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$
    if not(pattern.match(url)):
        raise forms.ValidationError("Enter a valid URL")'''

def validate_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except:
        raise forms.ValidationError("Enter a valid URL")

def validate_email(email):
    pattern = re.compile("^([a-z]+\.[a-z]{1})+(\@+mookambikainfo+\.com)$")
    if not(pattern.match(email)):
        raise forms.ValidationError("Enter a valid Email")

def validate_image(image):
    file_size = image.size
    limit_kb = 500
    if file_size > limit_kb * 1024:
        print("File is too large")
        raise forms.ValidationError("File is too large")
    else:
        print("file is small")

class BasicForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators = [validate_email])
    phone = forms.IntegerField(validators = [validate_phone])
    aadhar = forms.CharField(validators = [validate_aadhar])
    url = forms.URLField(validators = [validate_url])
    file = forms.FileField(validators = [validate_image])

