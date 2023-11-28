import streamlit as st


def display_error_box(valid_url: bool = False):
    if not valid_url:
        st.error("The URL is not valid", icon="🚨")
