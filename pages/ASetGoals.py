import streamlit as st

def calculate_bmi(weight, height):
    if height != 0:
        bmi = weight / ((height / 100) ** 2)  # BMI formula: weight (kg) / (height (m) * height (m))
        return bmi
    else:
        return 0

def adjust_goals(current_goals):
    # Sample logic for goal adjustment
    if current_goals[2] == "Weight Loss":
        # Check if user has achieved at least 50% of their target weight loss
        if current_goals[0] <= 0.5 * current_goals[3]:
            st.write("You've made significant progress! Consider adjusting your target weight loss.")
            st.write("Consult with a health professional for personalized recommendations.")
        else:
            st.write("Keep up the good work! Continue with your current target weight loss.")
    elif current_goals[2] == "Muscle Gain":
        # Check if user has achieved at least 50% of their target muscle gain
        if current_goals[0] >= 0.5 * current_goals[3]:
            st.write("You're making gains! It might be time to increase your target muscle mass.")
            st.write("Discuss with a fitness trainer for guidance on adjusting your goals.")
        else:
            st.write("Stay consistent with your workouts! Reevaluate your goals once you've made more progress.")
    elif current_goals[2] == "Endurance Improvement":
        # Check if user has achieved at least 50% of their target running distance
        if current_goals[0] >= 0.5 * current_goals[3]:
            st.write("You're building endurance! Consider setting a higher target running distance.")
            st.write("Speak with a running coach for advice on setting new goals.")
        else:
            st.write("Keep pushing your limits! Reassess your goals as you make further improvements.")
    elif current_goals[2] == "Overall Health":
        # Check if user has made any progress towards improving overall health
        st.write("Improving overall health is a continuous journey! Keep prioritizing your well-being.")
        st.write("Consult with a healthcare provider for personalized health recommendations.")

def run_fitness_goals_app():
    st.title("Goal Setting")

    if "weight" not in st.session_state:
        st.session_state.weight = 0.0
    if "height" not in st.session_state:
        st.session_state.height = 0.0

    weight = st.number_input("Weight (kg):", min_value=0.0, value=st.session_state.weight, key="weight_input")
    height = st.number_input("Height (cm):", min_value=0.0, value=st.session_state.height, key="height_input")

    st.session_state.weight = weight
    st.session_state.height = height

    bmi = calculate_bmi(weight, height)
    if bmi != 0:
        st.write(f"Your BMI: {bmi:.2f}")

    goal_options = ["Weight Loss", "Muscle Gain", "Endurance Improvement", "Overall Health"]
    selected_goal = st.selectbox("Select Fitness Goal:", goal_options, key="goal_select")

    st.write(f"You selected: {selected_goal}")
    st.write(f"Weight: {weight} kg, Height: {height} cm")

    goals_data = [weight, height, selected_goal]  # Store weight, height, and selected goal in a list

    if selected_goal == "Weight Loss":
        target_weight = st.number_input("Target Weight (kg):", min_value=0.0, key="target_weight_input")
        target_duration = st.number_input("Target Duration (weeks):", min_value=1, key="target_duration_input")
        st.write(f"Your target weight: {target_weight} kg")
        st.write(f"Target duration to achieve goal: {target_duration} weeks")
        goals_data.extend([target_weight, target_duration])  # Extend list with target weight and duration

    elif selected_goal == "Muscle Gain":
        target_muscle_mass = st.number_input("Target Muscle Mass (kg):", min_value=0.0, key="target_muscle_mass_input")
        target_duration = st.number_input("Target Duration (weeks):", min_value=1, key="target_duration_input")
        st.write(f"Your target muscle mass: {target_muscle_mass} kg")
        st.write(f"Target duration to achieve goal: {target_duration} weeks")
        goals_data.extend([target_muscle_mass, target_duration])  # Extend list with target muscle mass and duration

    elif selected_goal == "Endurance Improvement":
        target_running_distance = st.number_input("Target Running Distance (km):", min_value=0.0, key="target_running_distance_input")
        target_duration = st.number_input("Target Duration (weeks):", min_value=1, key="target_duration_input")
        st.write(f"Your target running distance: {target_running_distance} km")
        st.write(f"Target duration to achieve goal: {target_duration} weeks")
        goals_data.extend([target_running_distance, target_duration])  # Extend list with target running distance and duration

    elif selected_goal == "Overall Health":
        st.write("Improve overall health is a great goal!")

    if st.button("Save Goals"):
        st.write("Goals saved successfully!")
        adjust_goals(goals_data)  # Call function to provide goal adjustment recommendations

    return goals_data  # Return the list containing weight, height, and goals

if __name__ == "__main__":
    run_fitness_goals_app()
