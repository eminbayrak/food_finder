from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from actions.food_finder import FoodFinder
import geocoder
import requests


class ActionShowFoods(Action):
    def name(self) -> Text:
        return "action_show_foods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        _category = tracker.get_slot("food_category")
        if not _category:
            dispatcher.utter_message(
                text="Sorry I didn't get your food category")
            return [SlotSet("food_category", None)]

        # Finding the user's current location coordinates dynamically
        location = geocoder.ip('me')
        print("DEBUG: Current location:", location)  # Debugging line
        if location.ok:
            _location = f"{location.latlng[0]},{location.latlng[1]}"
            user_location = f" ({location.address})"
        else:
            # Use a default location if unable to get user's location
            _location = "37.7749,-122.4194"
            user_location = " (Default Location)"
            print("DEBUG: Default location used")  # Debugging line

        # Replace with your Google Maps API key
        _api_key = "AIzaSyAIlCeazuzVW6Fs2HEZhVvGPsznof-clWU"

        # Check if Google Maps API is working
        google_maps_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=0,0&radius=100&type=restaurant&key={_api_key}"
        try:
            response = requests.get(google_maps_url)
            response.raise_for_status()
            print("DEBUG: Google Maps API is working")
        except requests.exceptions.HTTPError as err:
            print(f"DEBUG: Google Maps API error - {err}")
            dispatcher.utter_message(
                text="Sorry, there was an error accessing the Google Maps API.")
            return []

        # Call FoodFinder class to find nearby places
        _places = FoodFinder.find_places_nearby(_location, _category, _api_key)
        if not _places:
            _text = f"Sorry, there are no {_category} restaurants near your location{user_location}."
            dispatcher.utter_message(text=_text)
            return [SlotSet("food_category", None)]

        _text = f"Here are some {_category} restaurants near your location{user_location}: "
        for _place in _places[:5]:  # show top 5 places
            _text += f"\n- {_place['name']}"
        dispatcher.utter_message(text=_text)

        return [SlotSet("food_category", None)]
