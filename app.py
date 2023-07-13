import streamlit as st
import time
from streamlit_tags import st_tags
from PIL import Image
import pymysql
import mysql.connector


st.set_page_config(
   page_title="Smart Resume Analyzer",
   page_icon='./Logo/images (2).png',
)
img = Image.open('./Logo/images (2).png')
# resized_img = img.resize((500, 500))

img = Image.open('./Logo/images (2).png')
resized_img = img.resize((800, 600))
st.title("Smart Resume Analyzer")
st.sidebar.markdown("# Choose User")
activities = ["User", "Admin"]
choice = st.sidebar.selectbox("Choose among the given options:", activities)

if choice == 'User':
    st.markdown('''<h5 style='text-align: left; color: #021659;'> "Unlock the power of your resume! Upload your document and unlock a world of smart recommendations."</h5>''', unsafe_allow_html=True)
    pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
    if pdf_file is not None:
        with st.spinner('Uploading your Resume...'):
            time.sleep(4)
        save_image_path = './Uploaded_Resumes/' + pdf_file.name


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='local',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)


