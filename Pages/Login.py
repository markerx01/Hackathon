import streamlit as st
import json

def main():
    # Page Configuration
    st.set_page_config(page_title="Authentication", page_icon="🔐", layout="centered")

    st.title("Welcome to Our App 🚀")

    # Create a sidebar for navigation
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Choose Action", menu)

    # --- LOGIN PAGE ---
    if choice == "Login":
        st.subheader("Login to your account")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        # Checkbox for "Remember Me" (visual only for this template)
        st.checkbox("Remember Me")

        if st.button("Login"):
            # Basic validation
            with open("DataBase.json", 'r') as db:
                data = json.load(db)
                if username in data.keys():
                    user = data[username]  # Checks if user with that username exists, if so adds to a var named user
                    if user and user["Password"] == password:
                        st.success(f"Logged in successfully! Welcome back, {username}.")
                    elif user and not user["Password"] == password:
                        st.warning("Incorrect password.")
                    else:
                        st.warning("Please enter both a username and a password.")
                else:
                    st.warning("User does not exist.")


    # --- SIGN UP PAGE ---
    elif choice == "Sign Up":
        st.subheader("Create a New Account")

        new_username = st.text_input("Choose a Username")
        new_email = st.text_input("Enter your Email")
        new_password = st.text_input("Create a Password", type='password')
        confirm_password = st.text_input("Confirm your Password", type='password')

        new_class = st.selectbox("Select grade:", ['11', '12'])
        subject = st.multiselect("Select your subjects", ['Math-3', 'Math-4', 'Math-5'])
        Population = st.multiselect("Select population your'e from:", ['Evacuated'])


        if st.button("Sign Up"):
            if not new_username or not new_email or not new_password:
                st.warning("Please fill out all the fields.")
            elif new_password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                data = {}
                with open("DataBase.json", 'r') as db:
                    data = json.load(db)
                payload = {
                    'Username': new_username,
                    'Email': new_email,
                    'Password': new_password,
                    'Class': new_class,
                    'Subjects': subject,
                    'Population': Population
                }
                with open("DataBase.json", 'w') as db:
                    data[new_username] = payload
                    json.dump(data, db)

                st.success(f"Account created successfully for {new_username}!")
                st.info("You can now select 'Login' from the sidebar menu to sign in.")
                st.balloons()


if __name__ == '__main__':
    main()
