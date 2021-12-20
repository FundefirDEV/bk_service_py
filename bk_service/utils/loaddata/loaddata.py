
import sys


# from pytest
from django.core.management import call_command


def setup_db(self):

    sysout = sys.stdout
    sys.stdout = open('filename.json', 'w')

    # Load locations
    call_command('loaddata', 'bk_service/locations/fixtures/locations.json')
    # Load Users
    call_command('loaddata', 'bk_service/users/fixtures/users.json')

    sys.stdout = sysout
