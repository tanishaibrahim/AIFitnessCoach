import streamlit as st

# Set page title and icon
st.set_page_config(page_title="AI Fitness Generator", page_icon=":muscle:")

# Header with icon
st.title(":muscle: Welcome to AI Fitness Trainer!")
st.write("This app helps you achieve your fitness goals with personalized plans and recommendations.")

# Features with icons
st.header("Features:")
st.write("- Set Fitness Goals: Define your fitness goals, such as weight loss, muscle gain, endurance improvement, or overall health.")
st.write("- Workout Routines: Generate customized workout routines tailored to your goals.")
st.write("- Nutrition Plan: Get personalized nutrition plans to complement your fitness goals.")
st.write("- Progress Tracker: Track your progress over time to stay motivated and monitor your achievements.")
st.write("- Workout Channels: Discover recommended workout channels on YouTube for additional guidance and motivation.")

# Instructions
st.header("Instructions:clipboard::")
st.write("1. Select a feature from the navigation menu.")
st.write("2. Follow the prompts to set your goals, generate workout routines, receive nutrition plans, track your progress, or explore workout channels.")