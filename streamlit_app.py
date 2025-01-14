import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames': {'utilisateur': 
   {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0,
   'logged_in': False,
   'role': 'utilisateur'},
   'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0,
   'logged_in': False,
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    st.title("Bienvenue sur ma page")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2w0eWllMXVxZjcwNmc3NzJwNGMxYjI4NDMwbDN6dzYxY3dpM3RndiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3rYN8z9FnEQqsTl6MX/giphy.gif")

def album_photo():
    st.title("Bienvenue sur mon album photo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.image("https://static.streamlit.io/examples/owl.jpg")

if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        message = st.text(f"Bienvenue {st.session_state['username']}")
        selection= option_menu(menu_title=None, options= ["Accueil", "Photos"], 
            icons=['house', 'cat'], menu_icon="cast", default_index=0)
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        album_photo()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
