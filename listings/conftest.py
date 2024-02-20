from django.core.management import call_command
import pytest


pytestmark = pytest.mark.django_db(transaction=True)


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    fixtures = ["api.json"]

    with django_db_blocker.unblock():
        for fixture in fixtures:
            call_command('loaddata', fixture)


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
