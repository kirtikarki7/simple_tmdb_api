import requests
from flask_restful import Resource

import settings


class BasicTmdb(Resource):
    def get(self, resource, resource_id, specific=None):
        tmdb_get_url = f"{settings.tmdb_base_url}/{settings.tmdb_api_version}/{resource}/{resource_id}/{specific}"
        if not specific:
            tmdb_get_url = f"{settings.tmdb_base_url}/{settings.tmdb_api_version}/{resource}/{resource_id}"
        api_key = settings.tmdb_api_key
        resp = requests.get(tmdb_get_url, params={'api_key': api_key})
        if not resp.status_code == 200:
            return resp.json(), resp.status_code
        return resp.json()
