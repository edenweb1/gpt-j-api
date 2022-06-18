import streamlit as st
import time
import requests


def main():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="French GPT-J demo",  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )
    st.title("French GPT-J Demo")
    """This app enables you to interact with large language models in a friendly way!"""

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
Triste, et le jour pour moi sera comme la nuit."""
       
    ]
    example = st.selectbox("Choisissez votre suggestion", ex_names)

    inp = st.text_area(
        "ou ecrivez votre propre suggestion ici!", example, max_chars=2000, height=150
    )

    try:
        rec = ex_names.index(inp)
    except ValueError:
        rec = 0

    with st.beta_expander("Options de generations"):
        length = st.slider(
            "Choose the length of the generated texts (in tokens)",
            2,
            1024,
            512 if rec < 2 else 50,
            10,
        )
        temp = st.slider(
            "Choose the temperature (higher - more random, lower - more repetitive). For the code generation or sentence classification promps it's recommended to use a lower value, like 0.35",
            0.0,
            1.5,
            1.0 if rec < 2 else 0.35,
            0.05,
        )

    response = None
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
                       
            st.text_area(rep, example, max_chars=2000, height=150
           

    if False:
        col1, col2, *rest = st.beta_columns([1, 1, 10, 10])

        def on_click_good():
            response["rate"] = "good"
            print(response)

        def on_click_bad():
            response["rate"] = "bad"
            print(response)

        col1.form_submit_button("👍", on_click=on_click_good)
        col2.form_submit_button("👎", on_click=on_click_bad)

    st.text("App baked with ❤️ by @edenweb1 and inspired by @vicgalle")


if __name__ == "__main__":
    main()
