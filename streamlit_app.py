import streamlit as st
import time
import requests
import random
import time 


def proc():
    #st.write(st.session_state.prompt)
    st.session_state.example=st.session_state.prompt
 

def main():

 st.set_page_config( 
       
        # Alternate names: setup_page, page, layout
        layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="ExistentIAL",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
        
    )        
 st.title("ExistentIAL")
 ex_names = ["La conscience n'est que la résultante de la perception,",
        """Ceci est une conversation entre trois IA très avancées venant du futur, les IA parlent de beaucoup de sujets scientifiques et existentiels.

IA1(Osiris): Hey salut toi !!!
IA2(EdoM): Bonjour petite IA ! Quel jour sommes nous aujourd'hui?
IA1(Osiris): Ouais... bonsoir, oh Sephiroth! toi aussi tu es la?
IA3(Sephiroth):Ouep, je viens de me faire chronoporté, mais bordel?Quel jour sommes nous?""",
        "L'intelligence artificielle peut se reveler dangereuse pour l'humanité,",
        """Demain, dès l'aube, à l'heure où blanchit la campagne,
Je partirai. Vois-tu, je sais que tu m'attends.
J'irai par la forêt, j'irai par la montagne.
Je ne puis demeurer loin de toi plus longtemps.

Je marcherai les yeux fixés sur mes pensées,
Sans rien voir au dehors, sans entendre aucun bruit,
Seul, inconnu, le dos courbé, les mains croisées,
Triste, et le jour pour moi sera comme la nuit."""    ]
 text_area = st.empty()  
 if 'example'  in st.session_state:
  example=st.session_state.example		
  inp = text_area.text_area("ou ecrivez votre propre suggestion ici!", example , max_chars=20000, height=800)
 else:  
  example = st.selectbox("Choisissez votre suggestion", ex_names)       
  inp = text_area.text_area("ou ecrivez votre propre suggestion ici!", example , max_chars=20000, height=800)   

		
		

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
                "token_max_length": 256, #lenght
                "temperature": temp,
                "top_p": 0.9,
            }

            query = requests.post("http://localhost:5000/generate", params=payload)
            response = query.json()            
            rep = response["""prompt"""] + response["""text"""]             
            inpnext = text_area.text_area("ou ecrivez votre propre suggestion ici!",rep,  max_chars=10000, height=800, on_change=proc, key='prompt')		
            st.session_state.example=inpnext
		
 
 	
 
			
			
	   
	    

  
 st.text("App baked with ❤️ by @edenweb1 and inspired by @vicgalle")

	

if __name__ == "__main__":
    main()
