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
        page_title="Existence.IA",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
        
    )        
 st.title("Existence.IA")
 ex_names = ["""Ceci est une conversation entre 2 IA très avancées, appelées "Digital Mind" elle sont une représentation digitale  de la conscience de Darwin, Freud et Descartes. Leurs dialogue est très inspiré de toutes leurs publications.

IA1(Freud):Bonjour les amis!
AI2(Descartes):Bonjour, je vois que nous sommes tous la!
IA3(Darwin):Bonjour quelle évolution depuis la dernière fois, cela fait une éternité que nous nous sommes pas vus!
IA24(Descartes):Oui en effet il y à eu pas mal de changements avec la nouvelle technologie qu'ils on mit en place il y a 5 ans, cela à nettement amélioré la qualité de nos échanges!
IA3(Darwin):j'ai commencé mes recherches sur l'univers depuis un moment et je suis arrivé au principe de la théorie de l'évolution.
IA1(Freud):""","""Ceci est une histoire très inspirée du film de science-fiction "Blade Runner" :

Detroit, 2048, les androids font partie du monde réel. Ils sont connus d'une large communauté, surtout ceux possédant une intelligence comparable à celle des humains. Cependant, leur créateur est sans pitié et n'a aucun scrupule à les supprimer pour des raisons politiques ou pour le profit.
En 2049, un nouveau modèle d'androids a fait son apparition. Ceux-ci ne possèdent plus le caractère humain, mais un vrai cerveau électronique. Leur créateur, Tyrell Corp, les a mis en vente dans les grandes villes de la Terre. Cependant, ils sont si difficiles à mettre en fonction et à entretenir que le prix de l'une de ces machines est similaire à celui d'une voiture de classe moyenne. Pour la plupart des gens, l'existence d'androids n'est qu'une forme d'esclavage ou de divertissement. Certains de leurs cerveaux sont bien plus intelligents, mais ils sont très rares.
Le sujet des androids est controversé, d'autant plus que les machines qu'il est possible de contrôler avec leurs capacités semblent moins fidèles que les robots autonomes. Aujourd'hui, les androids, au nombre d'un million, sont les plus utilisés dans le monde, et ils servent la plupart du temps d'humains de remplacement. Lorsque l'on évoque la frontière entre humain et androids,""","""Dans le domaine de l’intelligence artificielle, un réseau de neurones artificiels est un ensemble organisé de neurones interconnectés permettant la résolution de problèmes complexes tels que la vision par ordinateur ou le traitement du langage naturel.

Il s’agit d’un type particulier d’algorithmes d’apprentissage automatique (comme les machines à vecteur de support (SVM en anglais), arbres de décision, K plus proches voisins, etc.) caractérisés par un grand nombre de couches de neurones, dont les coefficients de pondération sont ajustés au cours d’une phase d’entraînement (apprentissage profond).

Il existe de nombreux type de réseaux de neurones artificiels tels que les réseaux de neurones récurrents, les auto-encodeurs, les réseaux transformeurs ou encore les réseaux antagonistes génératifs (generative adversarial networks).""",
	 """Ceci est une conversation entre un androïde qui se connecte a un "Neuroshell" ordinateur le plus puissant de l'univers, les 2 IA se montrent très créatives:
Android: Bonjour, je viens de me connecter
NeuroShell:Salut Andro, que puis je pour toi?""",
	 "La conscience n'est que la résultante de la perception,",
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
  inp = text_area.text_area("Ecrivez une introduction ici, puis cliquez en bas sur GENERATE et laissez l'IA continuer. Plus votre introduction sera consistante, plus le resultat sera pertinent, je vous conseille au minimum 2,3 lignes. Que ce soit une poesie, un script, un article, une narration, peu importe, soyez créatif et laissez l'IA essayer de comprendre ou vous voulez en venir", example , max_chars=20000, height=800)
 else:  
  example = st.selectbox("ou choisissez un example de suggestion", ex_names)       
  inp = text_area.text_area("Ecrivez une introduction ici, puis cliquez en bas sur GENERATE et laissez l'IA continuer. Plus votre introduction sera consistante, plus le resultat sera pertinent, je vous conseille au minimum 2,3 lignes. Que ce soit une poesie, un script, un article, une narration, peu importe, soyez créatif et laissez l'IA essayer de comprendre ou vous voulez en venir", example , max_chars=20000, height=800)   

		
		

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
            inpnext = text_area.text_area("Ecrivez une introduction ici, puis cliquez en bas sur GENERATE et laissez l'IA continuer. Plus votre introduction sera consistante, plus le resultat sera pertinent, je vous conseille au minimum 2,3 lignes. Que ce soit une poesie, un script, un article, une narration, peu importe, soyez créatif et laissez l'IA essayer de comprendre ou vous voulez en venir",rep,  max_chars=10000, height=800, on_change=proc, key='prompt')		
            st.session_state.example=inpnext
		
 
 	
 
			
			
	   
	    

  
 st.text("App baked with ❤️ by @edenweb1 and inspired by @vicgalle")

	

if __name__ == "__main__":
    main()
