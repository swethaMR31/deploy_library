from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    return render(request, "first_app/index.html",context =  date_dict)
    date_dict = {"access_records": webpages_list}