import streamlit as st
import trubrics 
import validators 

st.set_page_config(page_title='Palooza Wizard 🧙‍♂️', page_icon='🧙‍♂️', layout='wide')
st.title('Palooza Wizard 🧙‍♂️')

st.markdown("Palooza Wizard ✨ is a powerful tool that allows users to **create web scrapers with minimal effort**. With **just a URL as input**, this framework generates a Python script 🐍 that enables users to scrape data from a website of their choice 🌐.")
st.divider()

url = st.text_input("Input an URL", placeholder = "https://www.google.com/")
valid_url = (1 if validators.url(url) else 0)

if not valid_url:
    st.error('The URL is not valid', icon="🚨")
st.button("Continue", disabled = not valid_url)

with open("../outputs/citytourgirls_root__1__body__*__1__div__*__1__div__*__1__header__*__2__div__*__1__div__*__1__nav__*__1__ul__*.html", "r") as f:
    html = str(f.read())
st.components.v1.html(html, width = None, height = None, scrolling=True)
#user_feedback = trubrics.log_feedback(
#    component="default",
#    model=None,
#    prompt_id=None,
#    user_response={
#        "type": "thumbs",
#        "score": "👎",
#        "text": "Not a very funny joke...",
#    }
#)