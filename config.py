MAPBOX_ACCESS_TOKEN = "pk.eyJ1IjoiZGV2YW5qYiIsImEiOiJjbTRtdDh4OWMwMHllMmlzOTBrdzdmbTR6In0.N1Af1YkoBA3o0el7PRPkdQ"

GEOCODING_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json"
DIRECTIONS_URL = "https://api.mapbox.com/directions/v5/mapbox/walking/{}"

geocoding_req_params = {'access_token': MAPBOX_ACCESS_TOKEN}
directions_req_params = {'access_token': MAPBOX_ACCESS_TOKEN, 'geometries': "geojson"}