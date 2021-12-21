
import sys


# from pytest
from django.core.management import call_command


def setup_db(self, only_locations=False):

    sysout = sys.stdout
    sys.stdout = open('filename.json', 'w')

    # Load locations
    call_command('loaddata', 'bk_service/locations/fixtures/locations.json')

    if not only_locations:
        # Load Users
        call_command('loaddata', 'bk_service/users/fixtures/users.json')

    sys.stdout = sysout
