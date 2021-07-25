# streamlit main page
import streamlit as st
from multiapp import MultiApp
from apps import home, help

st.header("Login")
username = st.text_input("username")
password = st.text_input("password", type="password")

if username and password:
    loggedInUser = True
else:
    loggedInUser = False

st.write(f"User {username} is logged in with password {password}")

swv = {}
swv['abc'] = "World"
    
app = MultiApp(swv=swv)

# Add all your application here
app.add_app("Home", home.app)

if loggedInUser:
    app.add_app("Help", help.app)

# The main app
app.run()