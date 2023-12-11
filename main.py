from pathlib import Path
import streamlit as st
from st_pages import Page, add_page_title, show_pages

st.title('Smart Learn')

st.header('About')
st.markdown("***Smart Learn*** is a Data Science Project based on the topic of:<br><center>\"<span style='color:#0091D5'><span style='font-size:20px'>***Learning Object Classification Based On Personalisation***</span></span>\"</center>", unsafe_allow_html=True)


def italic_16px_text(text):
    color = "black"
    font_size = "16px"
    italic = True
    style = "font-size:{}; color:{}; font-style:italic;" if italic else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"

def col_17px_text(text):
    color = "#0091D5"
    font_size = "17px"
    bold = True
    italic = True
    style = "font-size:{}; color:{}; font-weight:bold; font-style:italic;" if bold else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"

about_text = f"""
<div style="text-align: justify;">
    <p>{italic_16px_text('Each individual possesses a unique approach to learning')}, also known as the {col_17px_text('learning style')}, and everyone has a distinct preference for specific learning objects. There exist various types of learning objects which we can choose to use as our medium to learn. With the variety of options, there appears to be a problem or {italic_16px_text('contemplation in choosing the right')} {col_17px_text('learning object')}.</p>
    <p>Research by Martin & Maria (2019), noted that {col_17px_text('personalisation')} is the key to improving learning performance. Furthermore, Imran et al. (2015) stated that {italic_16px_text('tailoring learning objects')} to align with students' individual learning styles and preferences can {italic_16px_text('enhance educational experience')} and {italic_16px_text('increase learners performance and satisfaction')}.</p>
</div>
"""
st.markdown(about_text, unsafe_allow_html=True)
        
from PIL import Image
LevelStudy_Gender = Image.open("Pictures/Personalisation.png")
st.image(LevelStudy_Gender, caption='Figure 1: High Level Overview of Personalisation Considerations', use_column_width="always")



show_pages([
    Page('main.py', 'Home'),
    Page('pages/vak.py', 'Details'),
#     Page('pages/LearningObjects.py', 'Learning Objects'),
    Page('pages/Questionaire.py', 'Which Learning Objects Suits Me Best?'),
    Page('pages/eda.py', 'Exploratory Data Analysis (EDA)'),
    Page('pages/UserManual.py', 'User Manual'),
])

