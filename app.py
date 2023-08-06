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




#CONNECT TO DATABASE

connection = pymysql.connect(host='localhost',user='root',password='local',db='db')
cursor = connection.cursor()


db_sql = """CREATE DATABASE IF NOT EXISTS db;"""
cursor.execute(db_sql)

    # Create table
    DB_table_name = 'user_data'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     Name varchar(500) NOT NULL,
                     Email_ID VARCHAR(500) NOT NULL,
                     resume_score VARCHAR(8) NOT NULL,
                     Timestamp VARCHAR(50) NOT NULL,
                     Page_no VARCHAR(5) NOT NULL,
                     Predicted_Field BLOB NOT NULL,
                     User_level BLOB NOT NULL,
                     Actual_skills BLOB NOT NULL,
                     Recommended_skills BLOB NOT NULL,
                     Recommended_courses BLOB NOT NULL,
                     PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)
    if choice == 'User':
        st.markdown('''<h5 style='text-align: left; color: #021659;'> Upload your resume, and get smart recommendations</h5>''',
                    unsafe_allow_html=True)
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        if pdf_file is not None:
            with st.spinner('Uploading your Resume...'):
                time.sleep(4)
            os.makedirs("Uploaded_Resumes", exist_ok=True)





