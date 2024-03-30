# Restaurant Recommender Chatbot

This is a chatbot project that suggests restaurants based on the user's food choice using the Google Maps API.

## Features

- Provides restaurant recommendations based on user's food choice.
- Utilizes the Google Maps API to search for nearby restaurants.

## Getting Started

To run this chatbot, follow these steps:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/eminbayrak/food_finder.git
   ```

2. Install the required dependencies by running:

   ```
   pip install -r requirements.txt
   ```

3. Generate a Google Maps API key from the [Google Cloud Console](https://console.cloud.google.com/) and replace `"YOUR_GOOGLE_MAPS_API_KEY"` in the `actions.py` file with your API key.

4. Train your Rasa model by running:

   ```
   rasa train
   ```

5. Run the Rasa action server:

   ```
   rasa run actions
   ```

6. Start the Rasa shell to interact with the chatbot:

   ```
   rasa shell
   ```

## Usage

Once the chatbot is running, you can interact with it in the Rasa shell. Here's an example conversation:

```
Your input -> hi
Bot: Hello! How can I help you today?
Your input -> show me Italian restaurants
Bot: Here are some Italian restaurants near your location:

- Restaurant 1
- Restaurant 2
- ...

Your input -> goodbye
Bot: Goodbye! Have a great day.
```
