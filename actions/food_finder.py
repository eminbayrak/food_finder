import requests
import json


class FoodFinder:
    @staticmethod
    def find_places_nearby(location, place_type, api_key):
        base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        params = {
            "location": location,  # format: "lat,lng"
            "radius": 5000,  # search places in a 5000m radius
            # type of place to search for (in this case, "restaurant")
            "type": place_type,
            "keyword": place_type,  # keyword to filter for Thai restaurants
            "key": api_key,  # your Google Maps API key
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            # Print response for debugging
            print("DEBUG: Google Maps API response:", response.text)
            res = response.json()
            if "results" in res:
                return res["results"]
            else:
                print("No results found in the response:", res)
                return []
        except requests.exceptions.RequestException as e:
            print("Error fetching nearby places:", e)
            return []
