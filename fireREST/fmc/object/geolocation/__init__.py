from fireREST.defaults import API_RELEASE_700, API_RELEASE_610
from fireREST.fmc import Resource


class GeoLocation(Resource):
    PATH = '/object/geolocations/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
