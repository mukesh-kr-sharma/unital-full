import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'unital.settings')

import django
django.setup()

from faker import Faker
from main_app.models import Notice
from faker.providers import lorem

fake = Faker()


def populate(N=5):
    for entry in range(N):
        fake_title = fake.sentence(nb_words=12, variable_nb_words=True, ext_word_list=None)
        fake_body = fake.sentence(nb_words=400, variable_nb_words=True, ext_word_list=None)
        fake_link = '#'
        # New Entry
        notice = Notice.objects.get_or_create(
            title=fake_title, body=fake_body, link=fake_link)[0]


if __name__ == "__main__":
    print("POPULATING NOTICE BOARD")
    populate(20)
    print("COMPLETE")
