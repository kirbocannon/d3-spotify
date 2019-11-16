# This is a python script that allows you to populate a json file ingestable by d3 force-directed graph. Data contains your Playlist/Track information from Spotify.

### 1.) Clone this repo
`KirboCannon >> git clone https://github.com/kirbocannon/d3-spotify` 
 
`KirboCannon >> cd d3-spotify`

### 2.) Setup virtual environment (optional)
```
KirboCannon >> virtualenv -p python3 venv
KirboCannon >> source venv/bin/activate
```

### 3.) Install requirements
`(venv) KirboCannon >> pip install -r requirements.txt`

### 4.) Create `credentials.yaml` file in the same directory as the spotify_script.py file
You must create your tokens using the Spotify developer site. Once you have this information, 
create the yaml file containing the credentials. 

```.env
username: {spotify_username}
client_id: {spotify_client_id}
client_secret: {spotify_client_secret}
```

### 5.) Run script and generate file
`(venv) KirboCannon >> python spotify_script /location/to/all/the/things`

### 6.) Nou you can import the postman collection and edit the collection variable to the URL of your data.