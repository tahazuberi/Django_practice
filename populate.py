import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

dummy = Faker()
topics = ['hello','games','house','places']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for i in range(n):

        top= add_topic()

        fakeurl = dummy.url()
        fakedate = dummy.date()
        fakename = dummy.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fakeurl,name=fakename)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fakedate)[0]

populate(15)

# if __name__ == '__main__':
#     print("populating script")

#     print("populating complete")