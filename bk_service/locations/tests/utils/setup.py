#  Django
from bk_service.locations.models.countries import Country
from bk_service.locations.models.states import State
from bk_service.locations.models.cities import City


def create_locations(country_name='Colombia', country_code='CO', state_name='Bogota', city_name='Bogota'):
    country = Country.objects.create(name=country_name, code=country_code)
    state = State.objects.create(name=state_name, country=country)
    city = City.objects.create(name=city_name, state=state)
    return city
