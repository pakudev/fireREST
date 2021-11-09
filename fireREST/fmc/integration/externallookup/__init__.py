from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class ExternalLookup(Resource):
    PATH = '/integration/externallookups/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640
