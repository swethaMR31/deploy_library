from django.shortcuts import render
from . forms import FormName

def form_name_view(request):
    form = FormName()
    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            print("Name: "+form.cleaned_data["name"])
            print("Email: "+form.cleaned_data["email"])
            print("Address: "+form.cleaned_data["text"])
    return render(request, "validation_app/form_name.html",{'form':form})
