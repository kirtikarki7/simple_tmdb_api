from app import app
import os
from unittest import mock

import pytest

# update env for testing (required before imports)
os.environ.update({
    "TMDB_API_KEY": "api_key",
    "TMDB_BASE_URL": "https://api_url.org",
    "TMDB_API_VERSION": "3",
    "APP_SECRET_KEY": "app_Key"
})


@mock.patch('requests.get')
def test_get_movie_details(mock_req):
    mock_req.return_value.json.return_value = {
        "id": 550,
        "imdb_id": "tt0137523",
        "original_language": "en",
        "original_title": "Title"
    }
    mock_req.return_value.status_code = 200
    client = app.test_client()
    url = 'movie/550'
    response = client.get(url)
    details = response.get_json()
    assert response.status_code == 200
    details['id'] == 550


@mock.patch('requests.get')
def test_movie_data_not_found(mock_req):
    mock_req.return_value.json.return_value = {
        "success": False,
        "status_code": 34,
        "status_message": "The resource you requested could not be found."
    }
    mock_req.return_value.status_code = 404
    client = app.test_client()
    url = 'movie/176512781'
    response = client.get(url)
    details = response.get_json()
    assert response.status_code == 404
    details['success'] == False
