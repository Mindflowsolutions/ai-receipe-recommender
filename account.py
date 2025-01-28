import streamlit as st
import pandas as pd
import plotly.express as px
import json
import re

# File paths
USER_DATA_FILE = "users.json"
FILE_PATH = "all_recipes_final_df_v2.csv"

# Function to load user data
def load_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Email validation
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Password validation
def is_valid_password(password):
    return len(password) >= 8

# Function to clean time columns (convert "15 mins" → 15)
def clean_time(value):
    if isinstance(value, str):
        match = re.search(r"(\d+)", value)  # Extract numbers
        return int(match.group(1)) if match else 0
    return int(value or 0)

# Load recipes
def load_recipes(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"❌ Error loading CSV file: {e}")
        return pd.DataFrame()

# Search function
def search_recipes(recipes, query):
    if not query:
        return pd.DataFrame()
    query_lower = query.lower()
    return recipes[
        recipes["name"].str.contains(query_lower, case=False, na=False) |
        recipes["ingredients"].str.contains(query_lower, case=False, na=False)
    ]

# Display recipe with graph
def display_recipe_with_graph(row):
    st.subheader(f"🍴 {row['name']}")
    st.write(f"**Category:** {row.get('category', 'N/A')}")
    st.write(f"**Summary:** {row.get('summary', 'N/A')}")
    st.write(f"**Rating:** {row.get('rating', 'N/A')} ({row.get('rating_count', '0')} ratings)")
    st.write(f"**Reviews:** {row.get('review_count', '0')}")
    st.write(f"**Ingredients:** {row.get('ingredients', 'N/A')}")

    # Directions
    directions = row.get('directions', '')
    if directions:
        st.write("**Directions:**")
        for step in directions.split("\n"):
            st.write(f"- {step.strip()}")

    # Convert time values
    prep_time = clean_time(row.get("prep", 0))
    cook_time = clean_time(row.get("cook", 0))
    servings = int(row.get("servings", 0) or 0)
    calories = float(row.get("calories", 0) or 0)

    # Graph
    graph_data = pd.DataFrame({
        "Attributes": ["Prep Time", "Cook Time", "Servings", "Calories"],
        "Values": [prep_time, cook_time, servings, calories]
    })

    fig = px.bar(graph_data, x="Attributes", y="Values", title=f"{row['name']} - Recipe Attributes")
    st.plotly_chart(fig)

# Main App
def app():
    st.title("AI Recipe Recommender")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    user_data = load_user_data()

    if not st.session_state.logged_in:
        choice = st.radio("Select an option:", ["Login", "Sign Up"], horizontal=True)

        if choice == "Login":
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            
            # Forgot Password Link
            forgot_password = st.button("Forgot Password?")
            if forgot_password:
                st.session_state.forgot_password = True  # Toggle the forgot password view

            if st.session_state.get("forgot_password", False):
                # Show reset password fields
                new_password = st.text_input("Enter your new password", type="password")
                confirm_new_password = st.text_input("Confirm your new password", type="password")
                reset_button = st.button("Reset Password")
                
                if reset_button:
                    if email in user_data:
                        if new_password == confirm_new_password:
                            if is_valid_password(new_password):
                                user_data[email]['password'] = new_password
                                save_user_data(user_data)
                                st.success("Your password has been successfully reset. Please log in with your new password.")
                                st.session_state.forgot_password = False  # Hide forgot password form
                            else:
                                st.error("Password must be at least 8 characters long.")
                        else:
                            st.error("Passwords do not match.")
                    else:
                        st.error("Email not found. Please sign up.")
                
            elif st.button("Login"):
                if email in user_data and user_data[email]['password'] == password:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.success("Login successful!")
                else:
                    st.error("Invalid email or password.")
                    
        else:  # Sign Up
            username = st.text_input("Username")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            if st.button("Sign Up"):
                if email in user_data:
                    st.error("Email already registered.")
                elif not is_valid_email(email):
                    st.error("Invalid email format.")
                elif password != confirm_password:
                    st.error("Passwords do not match.")
                elif not is_valid_password(password):
                    st.error("Password must be at least 8 characters long.")
                else:
                    user_data[email] = {"username": username, "password": password}
                    save_user_data(user_data)
                    st.success("Sign-up successful! Please log in.")

    else:
        st.subheader("Welcome to AI Recipe Recommender!")  # Removed "Welcome, Talha!"

        recipes = load_recipes(FILE_PATH)
        if recipes.empty:
            st.warning("No recipes available.")
            return

        query = st.text_input("Search recipes by name or ingredients")
        if query:
            results = search_recipes(recipes, query)
            if not results.empty:
                for _, row in results.iterrows():
                    display_recipe_with_graph(row)
            else:
                st.error("No matching recipes found.")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()  # Fixed logout issue

app()














            
        
        