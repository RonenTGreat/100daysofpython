import requests
from dotenv import load_dotenv
import os

load_dotenv()

HEIGHT = 160
WEIGHT = 73.5
GENDER = "male"
AGE = 23


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = os.getenv("APP_ID")
app_key = os.getenv("API_KEY")

user_exercise = input("Tell me which exercises did: ")

post_query = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

response = requests.post(url=nutritionix_endpoint, json=post_query, headers=headers)
print(response.json())
