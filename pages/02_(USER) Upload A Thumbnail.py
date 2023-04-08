import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
import json
import os
import time

# Setting background image (from LOCAL):

#with open('background.jpg', 'rb') as image_file:
    #encoded_string = base64.b64encode(image_file.read())
#st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#             background-size: cover
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#---------------------------------------------
try:
    f = open("logged_in.json")
    logged_in = json.load(f)
    #f.close()
    st.sidebar.markdown(f"Logged in as **{logged_in['username']}**")
    signOut = st.sidebar.button("Sign Out")
    if signOut:
        os.remove("logged_in.json")
    #----------------------------------------------------------------
    yt = Image.open('yt_play.png')
    col1, col2 = st.columns(2)

    with col1:
        st.title("Upload a Thumbnail.")
        st.markdown("Without a good thumbnail, you won't be able to maximise your video's potential.")
    with col2:
        uploaded_file = st.file_uploader("Upload your thumbnail here: ", type=['png','jpg'])
        #if uploaded_file is not None:
            #st.image(uploaded_file, caption='Image Preview')

    st.markdown("<hr>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)
    with col4:
        if uploaded_file is not None:
            st.image(uploaded_file, caption='Image Preview')
            st.write("Upload?")
            confirm = st.download_button("CONFIRM", data=uploaded_file, file_name=uploaded_file.name, mime=uploaded_file.type, use_container_width=True)
            #confirm = st.button("CONFIRM",use_container_width=True)
            if confirm:
                with st.spinner("Uploading..."):
                    time.sleep(1.5)
                    st.success("Done!")

except:
    st.title("You're not logged in")
    st.subheader("Please navigate to the login page from the sidebar to log in.")
    try:
        f.close()
        os.remove("logged_in.json")
    except:
        pass