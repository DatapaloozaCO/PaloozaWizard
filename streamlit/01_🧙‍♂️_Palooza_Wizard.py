import streamlit as st
import trubrics 
import validators 
import streamlit.components.v1 as components
import palooza_wizard as wizard

st.set_page_config(page_title='Palooza Wizard 🧙‍♂️', page_icon='🧙‍♂️', layout='wide')
st.title('Palooza Wizard 🧙‍♂️')

st.markdown("Palooza Wizard ✨ is a powerful tool that allows users to **create web scrapers with minimal effort**. With **just a URL as input**, this framework generates a Python script 🐍 that enables users to scrape data from a website of their choice 🌐.")
st.divider()
interacted = 0

url = st.text_input(
    "Input an URL", 
    placeholder = "https://www.google.com/", 
    value = ""
)
valid_url = (1 if validators.url(url) else 0)
if not valid_url and url != "":
    st.error('The URL is not valid', icon="🚨")
continue_button = st.button("Continue", disabled = not valid_url)


st.subheader("Wizard Results")
col1, col2 = st.columns(2)
with col1: 
    st.markdown("Node extracted")
    components.html("""
    <style>* {color: white;}</style>
    <ul class="menu" id="menu-lateral-movil"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-22656" id="menu-item-22656"><a href="https://startupeable.com/newsletter">Newsletter</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-7889" id="menu-item-7889"><a href="https://startupeable.com/podcast/">Podcast</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page current_page_parent menu-item-22657" id="menu-item-22657"><a href="https://startupeable.com/blog/">Blog</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6525" id="menu-item-6525"><a href="https://startupeable.com/glosario/">Glosario</a></li><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9603" id="menu-item-9603"><a href="https://startupeable.com/directorio/" rel="noopener" target="_blank">Directorio</a></li><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-16412" id="menu-item-16412"><a href="https://startupeable.com/tag/guias/">Más</a><ul class="sub-menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-16414" id="menu-item-16414"><a href="https://startupeable.com/anunciate/">Anúnciate</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4403" id="menu-item-4403"><a href="https://startupeable.com/equipo/">Acerca de</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21036" id="menu-item-21036"><a href="https://startupeable.com/lmv/">Linkedin Mínimo Viable</a></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21037" id="menu-item-21037"><a href="https://startupeable.com/angel-academy/">Angel Academy</a></li></ul></li></ul>
    """)
with col2: 
    st.markdown("Data preview")
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })
    agree = st.checkbox('I want this section')
    if agree:
        st.write('You have selected this section!')

st.button("Descargar mis datos 📁 en formato excel")