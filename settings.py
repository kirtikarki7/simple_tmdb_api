import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

tmdb_api_key = os.environ.get('TMDB_API_KEY')
tmdb_base_url = os.environ.get('TMDB_BASE_URL')
tmdb_api_version = os.environ.get('TMDB_API_VERSION')

app_secret_key = os.environ.get('APP_SECRET_KEY')