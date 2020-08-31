from django.shortcuts import render
from . forms import BasicForm

def index(request):
    form = BasicForm()
    if request.method == "POST":
        form = BasicForm(request.POST, request.FILES)
        if form.is_valid():
            print("Name: "+form.cleaned_data["name"])
            print("Email: "+form.cleaned_data["email"])
            print("Phone: "+str(form.cleaned_data["phone"]))
            print("Aadhar: "+form.cleaned_data["aadhar"])
            print("URL: "+form.cleaned_data["url"])
            print("File: "+str(form.cleaned_data["file"]))
    return render(request, "form_validation_app/index.html",{'form':form})
