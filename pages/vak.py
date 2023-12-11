import streamlit as st

st.title('Learning Style and Objects', anchor=False)


# st.markdown("Learning Style is a way of classifying the different <span style='color:blue'>***ways people learn***</span> and <span style='color:blue'>***how they approach information***</span> (Sreenidhi and Tay, 2017)", unsafe_allow_html=True)

# st.markdown("According to research by Sreenidhi and Tay, 2017, the Fleming’s VARK model, provides the learners with a <span style='color:blue'>***profile of their learning styles***</span>. Learners are able to <span style='color:blue'>***understand the type of learning that best suits them***</span>. People learn by:  ", unsafe_allow_html=True)

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


st.header('VAK Learning Style', anchor=False)
ls_text = f"""
<div style="text-align: justify;">
    <p>Learning Style is a way of classifying the different {col_17px_text('ways people learn')} and {col_17px_text('how they approach information')} (Sreenidhi and Tay, 2017). There are many types of learning style and this project focuses on the {italic_16px_text('VAK Learning Style')}.</p>
</div>
"""
st.markdown(ls_text, unsafe_allow_html=True)

vak_text = f"""
<div style="text-align: justify;">
    <p>According to research by Sreenidhi and Tay, 2017, the Fleming’s VARK model, provides the learners with a {col_17px_text('profile of their learning styles')}. Learners are able to {col_17px_text('understand the type of learning that best suits them')}. People learn by:</p>
</div>
"""
st.markdown(vak_text, unsafe_allow_html=True)

vak = """
- Seeing  (<u>**V**</u>isual)
- Hearing  (<u>**A**</u>uditory)
- Doing (<u>**K**</u>inesthetic)
"""
st.markdown(vak, unsafe_allow_html=True)
    

            

st.header('Learning Object', anchor=False)

lo_text = f"""
<div style="text-align: justify;">
    <p>According to Quinn and Hobbs, 2000, the IEEE’s Learning Technology Standards Committee defines ’learning objects’ as entities, whether {col_17px_text('digital')} or {col_17px_text('non-digital')}, that can be harnessed, reused, or {col_17px_text('referenced')} in the context of {col_17px_text('technology-supported learning')}. </p>
</div>
"""
st.markdown(lo_text, unsafe_allow_html=True)

st.write('Below are some types of learning objects.')

st.subheader('Animated Instruction', anchor=False)
st.write('Visual instruction employing animation techniques, used to simplify complex concepts, processes, or explanations through engaging animated content.')

st.subheader('Audio-Recorded Lecture', anchor=False)
st.write('Recordings of lectures or talks in audio format, allowing learners to listen to educational content, speeches, or discussions related to a specific topic.')

st.subheader('Book', anchor=False)
st.write('Educational content presented in the form of a traditional book, providing in-depth information, theories, examples, and exercises related to a particular subject or topic.')

st.subheader('Educational Game', anchor=False)
st.write('Interactive activities designed for learning purposes, often incorporating challenges, puzzles, or simulations to educate and engage learners in a fun and interactive way.')

st.subheader('Intelligent Computer-Aided Instruction Systems', anchor=False)
st.write('Advanced systems employing artificial intelligence or adaptive learning techniques to personalize instruction, tailor content to individual learners, and track progress effectively.')

st.subheader('Interactive Tool', anchor=False)
st.write('Software applications, simulations, or online tools designed to actively engage learners by allowing them to manipulate content and interact with the learning materials.')

st.subheader('Lecture Notes', anchor=False)
st.write('Concise summaries or written materials derived from lectures, capturing key points, explanations, and essential information delivered during a lecture session.')

st.subheader('Mind Map', anchor=False)
st.write('Graphic organizers presenting information or concepts hierarchically, often using branching or radial diagrams to depict connections and relationships between ideas.')

st.subheader('Multimedia Content', anchor=False)
st.write('Educational materials integrating various media elements such as text, images, audio, and video to provide a comprehensive learning experience.')

st.subheader('Real Object Model', anchor=False)
st.write('Physical models or real-world objects used in education to illustrate concepts, structures, or systems in a tangible and interactive manner.')

st.subheader('Slide Presentation', anchor=False)
st.write('A visual presentation created using software like PowerPoint or Google Slides, typically consisting of slides containing information, images, and graphics to convey a message or lesson.')

st.subheader('Technology-Supported Learning Include Computer-Based Training Systems', anchor=False)
st.write('Learning systems or software utilizing technology, including computer-based programs or online platforms, to facilitate educational content delivery and assessment.')

st.subheader('Video', anchor=False)
st.write('Visual content that can include lectures, demonstrations, experiments, or educational content presented in a video format, allowing learners to visually grasp complex concepts.')

# from PIL import Image
# LevelStudy_Gender = Image.open("Pictures/LevelStudy_Gender.png")
# st.image(LevelStudy_Gender, caption='Figure 1: Level of Study & Gender', use_column_width="always")

# VAK_Distributions = Image.open("Pictures/VAK_Distributions.png")
# st.image(VAK_Distributions, caption='VAK Distributions', use_column_width="always")

# Preferred_LearningMode = Image.open("Pictures/Preferred_LearningMode.png")
# st.image(Preferred_LearningMode, caption='Preferred Learning Mode Based On a Dominant VAK', use_column_width="always")

# Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
# st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

# Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
# st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

# Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")
# st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")

# # Load the images
# # Preferred_LO_Visual = Image.open("Pictures/Preferred_LO_Visual.png")
# # Preferred_LO_Auditory = Image.open("Pictures/Preferred_LO_Auditory.png")
# # Preferred_LO_Kinesthetic = Image.open("Pictures/Preferred_LO_Kinesthetic.png")

# # Display images in a 3-column layout
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.image(Preferred_LO_Visual, caption='Preferred Learning Objects (Visual)', use_column_width="always")

# with col2:
#     st.image(Preferred_LO_Auditory, caption='Preferred Learning Objects (Auditory)', use_column_width="always")

# with col3:
#     st.image(Preferred_LO_Kinesthetic, caption='Preferred Learning Objects (Kinesthetic)', use_column_width="always")
