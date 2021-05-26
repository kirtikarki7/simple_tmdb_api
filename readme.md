## Simple TMDB API.

### Purpose -
Simple TMDB API is a proxy api to TMDB API and simplifies the way to use it so our mobile application won't have to deal with it directly. It is also to own api credentials in order to avoid exposing it by malicious extraction from app.

### Getting Started -
Documentation: https://developers.themoviedb.org/3/getting-started/introduction
Register for an account on the TMBD API above and acquire your API_KEY following the instructions.

### Endpoints -

- `GET` **/<string:resource>/<int:resource_id>** - To get all details of a single resource. Usage example - **/movie/550**
- `GET` **/<string:resource>/<int:resource_id>/<string:specific>** - To get specific details of a single resource. Usage example - **/movie/550/keywords**

### Development Approach - 
1. Decided to use flask_restful for implementation of Simple TMDB API as we just have to implement a simple proxy to serve data from TMDB API.
2. Following the TDD approach, firstly created unittests for the endpoint which fetches data from TMDB API.
3. Created get method for resource of **/<string:resource>/<int:resource_id>** endpoint to interact with TMDB API.
4. Modified get method of BasicTMDB resource to fetch specific details of a resource as well.
5. Added basic logging for the flask server.


### Run Commands - 

- The requirements for this project are in `simple_tmdb_api`. 

- Create a `.env` file in your project folder and pass variables there.

```bash
# TMDB CREDS
TMDB_API_KEY=API_KEY_HERE
TMDB_BASE_URL=https://api.themoviedb.org
TMDB_API_VERSION=3

# OTHERS
APP_SECRET_KEY=API_SECRET_KEY_HERE
```

<br>

```bash

# (recommended) create a conda env
conda create -n env_sda python=3.7
conda activate env_sda

# get inside of project dir
cd simple_tmdb_api

#install requirements for development
pip install -r requirements.txt

# run flask server
python app.py

# run unit tests
pytest

```
