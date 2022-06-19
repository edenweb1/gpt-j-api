import streamlit as st
import time
import requests
import random

st.set_page_config( 
       
        # Alternate names: setup_page, page, layout
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="French GPT-J dem0",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
        
    )        
st.title(str(random.random()))
ex_names = [
        "En termes simples, l'intelligence artificielle (IA) fait référence à des systèmes ou des machines qui imitent l'intelligence humaine pour effectuer des tâches et qui peuvent s'améliorer en fonction des informations collectées grâce à l'itération.",
        "The ancient people of Arcadia achieved oustanding cultural and technological developments. Below we summarise some of the highlights of the Acadian society.",
        """Demain, dès l'aube, à l'heure où blanchit la campagne,
Je partirai. Vois-tu, je sais que tu m'attends.
J'irai par la forêt, j'irai par la montagne.
Je ne puis demeurer loin de toi plus longtemps.

Je marcherai les yeux fixés sur mes pensées,
Sans rien voir au dehors, sans entendre aucun bruit,
Seul, inconnu, le dos courbé, les mains croisées,
Triste, et le jour pour moi sera comme la nuit."""    ]


example = st.selectbox("Choisissez votre suggestion", ex_names)


	
text_area = st.empty()

if 'example' not in st.session_state:
       
 inp = text_area.text_area("ou ecrivez votre propre suggestion ici!", example , max_chars=20000, height=600)   
else:
 #st.write(st.session_state.example)	
 inp = text_area.text_area("ou ecrivez votre propre suggestion ici!", st.session_state.example , max_chars=20000, height=600) 
		
		

with st.beta_expander("Options de generations"):
        length = st.slider(
            "Choose the length of the generated texts (in tokens)",
            2,
            1024,
            512 ,
            10,
        )
        temp = st.slider(
            "Choose the temperature (higher - more random, lower - more repetitive). For the code generation or sentence classification promps it's recommended to use a lower value, like 0.35",
            0.0,
            1.5,
            1.0 ,
            0.05,
        )
##response = None
with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Generate!")

        if submit_button:

            payload = {
                "context": inp,
                "token_max_length": length,
                "temperature": temp,
                "top_p": 0.9,
            }

            query = requests.post("http://localhost:5000/generate", params=payload)
            response = query.json()            
            rep = response["""prompt"""] + response["""text"""]             
            inp = text_area.text_area("ou ecrivez votre propre suggestion ici!",rep,  max_chars=10000, height=600)
	    
            st.session_state.example = rep
   

st.text("App baked with ❤️ by @edenweb1 and inspired by @vicgalle")


