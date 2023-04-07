import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64

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
with col3:
    pass
with col4:
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Image Preview')
with col5:
    pass