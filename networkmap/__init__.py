import streamlit as st
from networkmap import visualize

def render_page():

    #Page-Title
    st.set_page_config(page_title = 'STNM',page_icon = "random", layout="centered")

    #Title
    st.markdown("<h1 style='text-align: center; color: White;'>Search Term Network Map</h1>", unsafe_allow_html=True)

    #Header
    st.header("Enter Search Term")

    #SearchBox
    searchterm=st.text_input("","Type Here",help='Search is case in-sensitive')


    #Search Button
    if st.button("SEARCH"):

        holder = st.empty()

        #Loading
        with st.spinner('Fetching from cloud...'):
            holder.empty()

            #Confirming if the search term is present
            if visualize.ret1(searchterm) != -1:

                #Opening the newly created outputfile
                file = open('networkmap/output.html','r',encoding='utf-8')
                file = file.read()

                #Displying the network tree/map
                import streamlit.components.v1 as components
                components.html(file,height=900)

            else:

                #If search term not registered in database
                holder.error("**Phrase not found. \nWill try to add soon.**")
