import streamlit as st

# Titre
st.title("Mon premier Streamlit 🎉")

# Texte
st.write("Ceci est une application Streamlit très simple.")

# Saisie utilisateur
nom = st.text_input("Quel est ton nom ?")

# Bouton
if st.button("Dire bonjour"):
    st.success(f"Bonjour {nom} 👋")
