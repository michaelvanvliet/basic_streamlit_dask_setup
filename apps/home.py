import streamlit as st

def app(swv):

    st.title(f"Home {swv['abc']}")

    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")

    add_selectbox = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    st.write(add_selectbox)