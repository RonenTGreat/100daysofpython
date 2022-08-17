import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

HEIGHT = 160
WEIGHT = 73.5
GENDER = "male"
AGE = 23

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/bacad1c9188a01ac0462d5ad836c9089/myWorkouts/workouts"

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

today = datetime.now()


response = requests.post(url=nutritionix_endpoint, json=post_query, headers=headers)
exercise_data = response.json()

for exercise in exercise_data["exercises"]:
    sheet_input = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response_exercise = requests.post(url=sheet_endpoint, json=sheet_input, auth=("ronen", "bnVsbDpudWxs"))
    print(response_exercise.text)
