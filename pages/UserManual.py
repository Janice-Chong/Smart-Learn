import streamlit as st

st.title('User Manual', anchor=False)

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

quick_guide = f"""
<div style="text-align: justify;">
    <p>Here's a {col_17px_text('quick guide')} to use {italic_16px_text('Smart Learn')}.</p>
</div>
"""
st.markdown(quick_guide, unsafe_allow_html=True)

steps = f"""
<div style="text-align: justify;">
    <ol>
        <li>Go through the {italic_16px_text('Documentation of Each Tab')} below to get an overview of the functionality of each tab.</li>
        <li>Get an understanding of {italic_16px_text('Smart Learn')} by reading through the {italic_16px_text('Home')} and {italic_16px_text('Details')} tab.</li>
        <li>Learn your learning style and the learning objects that suits you best by answering the questionaire in the {italic_16px_text('Which Learning Objects Suits Me Best?')} tab.</li>
    </ol>
</div>
"""
st.markdown(steps, unsafe_allow_html=True)

st.header('Documentation of Each Tab', anchor=False)
st.subheader('Home Tab')
home_tab = f"""
<div style="text-align: justify;">
    <p>Contains information on the {col_17px_text('background')} of {italic_16px_text('Smart Learn')}.</p>
</div>
"""
st.markdown(home_tab, unsafe_allow_html=True)

st.subheader('Details Tab', anchor=False)
vak_tab = f"""
<div style="text-align: justify;">
    <p>Contains {col_17px_text('2 parts')}: </p>
</div>
"""
st.markdown(vak_tab, unsafe_allow_html=True)

details_part = """
- VAK Learning Style
    - Consists of information on the definition and the purpose of the learning style
- Learning Objects
    - Describe the learning objects used in this project and their respective definitions
"""
st.markdown(details_part, unsafe_allow_html=True)



st.subheader('Which Learning Objects Suits Me Best? Tab', anchor=False)
question_tab = f"""
<div style="text-align: justify;">
    <p>Consists of a {col_17px_text('questionaire')} where users can fill in the questionaire to {col_17px_text('find out their dominant VAK')} learning style and get a or some learning objects recommendations which suits their learning style. This may be helpful for users who are {col_17px_text('looking to seek learning objects which suits their learning style to help them learn more efficiently')}. After answering the questionaire, the system will:</p>
</div>
"""
st.markdown(question_tab, unsafe_allow_html=True)

sys_will = """
- Determine user's dominant VAK learning style (i.e. either Visual, Auditory or Kinesthetic)
- Recommend learning object(s)
"""
st.markdown(sys_will, unsafe_allow_html=True)

st.subheader('Exploratory Data Analysis (EDA) Tab', anchor=False)
eda_tab = f"""
<div style="text-align: justify;">
    <p>Describe the data collected in regards to the project, to show the general {col_17px_text('distribution of the respondents')} (e.g. gender, level of study, dominant learning style) as well as the {col_17px_text('general preferences')} on the learning mode and learning objects.</p>
</div>
"""
st.markdown(eda_tab, unsafe_allow_html=True)


st.subheader('User Manual Tab', anchor=False)
manual_tab = f"""
<div style="text-align: justify;">
    <p>This tab is the current tab you are viewing and as the name suggest, it provides users a guide and information on the {col_17px_text('functionality')} of this website.</p>
</div>
"""
st.markdown(manual_tab, unsafe_allow_html=True)



