import json

from six import iteritems

from tvdb_api_v2.api_client import ApiClient
from tvdb_api_v2.apis.authentication_api import AuthenticationApi
from tvdb_api_v2.apis.search_api import SearchApi
from tvdb_api_v2.configuration import Configuration
from tvdb_api_v2.models.auth import Auth
from tvdb_api_v2.models.series_search_data import SeriesSearchData

API_KEY = "9710D6F39C4A2457"
HOST = "https://api.thetvdb.com"


class TvdbClient(object):
    def __init__(self):
        # setup configuration
        self.configuration = Configuration()
        self.configuration.host = HOST
        self.configuration.api_key_prefix['Authorization'] = 'Bearer'
        # create tvdb_client
        self.api_client = ApiClient()

    def authenticate(self):
        token = AuthenticationApi(self.api_client).login_post(Auth(API_KEY))
        self.configuration.api_key['Authorization'] = token.token

    def search_series_by_name(self, series_name, best_result=False):
        params = {'name': series_name, '_preload_content': True}
        return SearchApi(self.api_client).search_series_get(**params)

    def search_series_by_id(self, imdb_id):
        params = {'imdb_id': imdb_id, '_preload_content': True}
        return SearchApi(self.api_client).search_series_get(**params)

    ####################################################################################################################

    # Use this if we want to parse the response ourselves -> set 'preload_content' = False in params
    def _parse_search_series_data(self, response, best_result=False):
        data = json.loads(response.data)
        # json object is a dict with a data key which contains a list of SeriesSearchData
        search_results = data['data'] if 'data' in data.keys() else None
        if best_result:
            return self._deserialize_model(search_results[0], SeriesSearchData())
        else:
            return [self._deserialize_model(result, SeriesSearchData()) for result in search_results]

    def _deserialize_model(self, data, instance):
        if not instance.swagger_types:
            return data
        for attr, attr_type in iteritems(instance.swagger_types):
            if data is not None and instance.attribute_map[attr] in data and isinstance(data, (list, dict)):
                value = data[instance.attribute_map[attr]]
                setattr(instance, attr, value)
        return instance
