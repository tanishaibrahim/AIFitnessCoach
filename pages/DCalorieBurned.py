# progress_tracker.py

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import datetime

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class ProgressTracker:
    def _init_(self):
        self.model = genai.GenerativeModel("gemini-pro")

    def get_gemini_response(self, question):
        chat = self.model.start_chat(history=[])
        response = chat.send_message(question, stream=True)
        return response

    def calculate_calories_burned(self, exercise_type, duration, weight):
        # Calorie calculation logic based on exercise type, duration, and weight
        # This logic needs to be implemented based on established formulas or APIs
        # For demonstration, let's assume a simple formula: calories burned = duration (minutes) * weight (kg)
        calories_burned = duration * weight
        return calories_burned

    def main(self):
        # Set page config
        st.set_page_config(page_title="Calories Burned Calculator")

        st.title("Calories Burned Calculator")

        # Exercise input section
        exercise_type = st.selectbox("Select Exercise Type:", ["Running", "Cycling", "Weightlifting", "Skipping"])
        duration = st.number_input("Duration (minutes):", min_value=0)
        weight = st.number_input("Weight (kg):", min_value=0)

        if st.button("Calculate Calories Burned"):
            calories_burned = self.calculate_calories_burned(exercise_type, duration, weight)
            st.write(f"Calories burned: {calories_burned} kcal")

# Usage
tracker = ProgressTracker()
tracker.main()