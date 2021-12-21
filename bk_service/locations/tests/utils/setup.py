#  Django
from bk_service.locations.models.countries import Country
from bk_service.locations.models.states import State
from bk_service.locations.models.cities import City


def create_locations(countryName='Colombia', countryCode='CO', stateName='Bogota', cityName='Bogota'):
    country = Country.objects.create(name=countryName, code=countryCode)
    state = State.objects.create(name=stateName, country=country)
    city = City.objects.create(name=cityName, state=state)
    return city
