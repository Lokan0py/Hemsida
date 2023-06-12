#import requests
import streamlit as st
#from streamlit_lottie import st_lottie

# startas genom att skriva: streamlit run hemsida.py 
# se till att vara i rätt filmapp 

st.set_page_config(page_title="Min hemsida", page_icon=":globe_with_meridians:", layout="wide")

"""def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()"""

# Use CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# lottiefiles
#lottie_stock = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3kjzsbjv.json")
#lottie_energy = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_v0qottlc.json")

# Första rubrik
with st.container():
    st.subheader("Hej, mitt namn är Simon :wave:")
    st.title("Studerar på KTH till civilingenjör inom energi och miljö")
    st.write("Jag har ett intresse för energi, börs och träning")

# Favorit hemsidor
with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.header("Favorit hemsidor")
        st.subheader("[Kontrollrummet](https://www.svk.se/om-kraftsystemet/kontrollrummet)")
        #st.write("##")
        st.subheader("[Electricity maps](https://app.electricitymaps.com/map)")
        #st.write("##")
        st.subheader("[Avanza](https://www.avanza.se/hem/hem.html)")
    """
    with middle_column:
        st_lottie(lottie_energy, height=300, key="energy")
    
    with right_column:
        st_lottie(lottie_stock, height=300, key="stock")"""

# Kontakt 
with st.container():
    st.write("---")
    st.header("Kom i kontakt med mig!")
    #st.write("##")

    # https://formsubmit.co/
    contact_form = """<form action="https://formsubmit.co/simon.ahling@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Ditt namn" required>
     <input type="email" name="email" placeholder="Din email" required>
     <textarea name="message" placeholder="Ditt meddelande" required></textarea>
     <button type="submit">Skicka</button>
    </form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



