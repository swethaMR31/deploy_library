import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_with_models.settings')
django.setup()


import random
from faker import Faker
from first_app.models import Topic, AccessRecord, Webpage
#from working_with_models.first_app import models


fakegen = Faker()

topics = ["search", "social", "market", "news", "games"]

def add_topic():
    topic = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    topic.save()
    return topic

def populate(NUMBER = 5):
    for entry in range(NUMBER):
        #get topic for entry
        topic_result = add_topic()
        #fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic = topic_result, url = fake_url, name = fake_name)[0]
        access_record = AccessRecord.objects.get_or_create(name = webpage, date = fake_date)[0]

if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Population completed!")


