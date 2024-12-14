import json
import requests
import urllib.parse
import textwrap
from config import GEOCODING_URL, geocoding_req_params

def get_geocoding_options(search_query):
    """
    Fetch geocoding options based on a search query.

    Args:
        search_query (str): The query string to search for geocoding options.

    Returns:
        list[dict]: A list of options, each containing a 'label' and 'value'.
    """
    if not search_query:
        return []

    try:
        # Encode the search query for safe usage in a URL
        search_query = urllib.parse.quote(search_query)
        req_url = GEOCODING_URL.format(search_query)

        # Send the request to the geocoding API
        response = requests.get(req_url, params=geocoding_req_params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Extract and format options from the response
        features = response.json().get("features", [])
        options = [
            {
                "label": textwrap.shorten(
                    feature.get("place_name", "Unknown"), 
                    width=55, 
                    placeholder="..."
                ),
                "value": json.dumps(feature)
            }
            for feature in features
        ]
        return options

    except requests.exceptions.RequestException as e:
        print(f"Error fetching geocoding options: {e}")
        return []

    except KeyError as e:
        print(f"Unexpected response format: {e}")
        return []
