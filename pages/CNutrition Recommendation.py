import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    chat = model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response


# Initialize Streamlit app
st.set_page_config(page_title="Nutrition Recommendation")
st.title("Nutrition Plan")

# Input for meal type
goal_type = st.selectbox("Select your fitness goal:", ["Weight loss", "Muscle gain", "Endurance improvement", "Overall health and wellness"])

# Button to generate recipe
submit_button = st.button("Generate Nutrition Plan")

# Check if input_text is not empty and button is clicked
if goal_type and submit_button:
    st.subheader("Here's the Nutrition Plan:")
    # Create prompt based on user inputs
    prompt = f"Generate a nutrition plan for {goal_type.lower()} "
    response = get_gemini_response(prompt)
    for chunk in response:
        st.write(chunk.text)