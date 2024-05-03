import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate workout recommendations
def generate_workout_channels(goal_type):
    # Initialize GenerativeAI model
    model = genai.GenerativeModel("gemini-pro")
    
    # Generate prompt
    prompt = f"Generate YouTube workout channels for {goal_type.lower()} "
    
    # Start conversation and get response
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt, stream=True)
    
    # Return response
    return response

# Initialize Streamlit app
st.set_page_config(page_title="YouTube Workout Recommendations")
st.title("Workout Channel Recommendations")

# Input for fitness goal
goal_type = st.selectbox("Select your fitness goal:", ["Weight loss", "Muscle gain", "Endurance improvement", "Overall health and wellness"])

# Button to generate workout channels
submit_button = st.button("Generate Workout Channels")

# Check if fitness goal is selected and button is clicked
if goal_type and submit_button:
    st.subheader("Here are the recommended YouTube workout channels:")
    # Generate and display workout channels
    response = generate_workout_channels(goal_type)
    for chunk in response:
        st.write(chunk.text)