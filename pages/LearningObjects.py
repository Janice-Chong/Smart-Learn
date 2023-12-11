import streamlit as st

st.title('Learning Objects')
st.text('What are learningobjects? Types of learning objects')

def col_17px_text(text):
    color = "#0091D5"
    font_size = "17px"
    bold = True
    italic = True
    style = "font-size:{}; color:{}; font-weight:bold; font-style:italic;" if bold else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"

st.header('What is Learning Object?')
# st.write('According to Quinn and Hobbs, 2000, the IEEE’s Learning Technology Standards Committee defines ’learning objects’ as entities, whether digital or non-digital, that can be harnessed, reused, or referenced in the context of technology-supported learning.')
# st.markdown("According to Quinn and Hobbs, 2000, the IEEE’s Learning Technology Standards Committee defines ’learning objects’ as entities, whether <span style='color:blue'><span style='font-size:20px'>digital</span></span> or <span style='color:blue'><span style='font-size:20px'>non-digital</span></span>, that can be harnessed, reused, or <span style='color:blue'><span style='font-size:20px'>referenced</span></span> in the context of <span style='color:blue'><span style='font-size:20px'>technology-supported learning</span></span>.", unsafe_allow_html=True)

lo_text = f"""
<div style="text-align: justify;">
    <p>According to Quinn and Hobbs, 2000, the IEEE’s Learning Technology Standards Committee defines ’learning objects’ as entities, whether {col_17px_text('digital')} or {col_17px_text('non-digital')}, that can be harnessed, reused, or {col_17px_text('referenced')} in the context of {col_17px_text('technology-supported learning')}. </p>
</div>
"""
st.markdown(lo_text, unsafe_allow_html=True)

st.write('Below are some types of learning objects.')

st.subheader('Animated Instruction')
st.write('Visual instruction employing animation techniques, used to simplify complex concepts, processes, or explanations through engaging animated content.')

st.subheader('Audio-Recorded Lecture')
st.write('Recordings of lectures or talks in audio format, allowing learners to listen to educational content, speeches, or discussions related to a specific topic.')

st.subheader('Book')
st.write('Educational content presented in the form of a traditional book, providing in-depth information, theories, examples, and exercises related to a particular subject or topic.')

st.subheader('Educational Game')
st.write('Interactive activities designed for learning purposes, often incorporating challenges, puzzles, or simulations to educate and engage learners in a fun and interactive way.')

st.subheader('Intelligent Computer-Aided Instruction Systems')
st.write('Advanced systems employing artificial intelligence or adaptive learning techniques to personalize instruction, tailor content to individual learners, and track progress effectively.')

st.subheader('Interactive Tool')
st.write('Software applications, simulations, or online tools designed to actively engage learners by allowing them to manipulate content and interact with the learning materials.')

st.subheader('Lecture Notes')
st.write('Concise summaries or written materials derived from lectures, capturing key points, explanations, and essential information delivered during a lecture session.')

st.subheader('Mind Map')
st.write('Graphic organizers presenting information or concepts hierarchically, often using branching or radial diagrams to depict connections and relationships between ideas.')

st.subheader('Multimedia Content')
st.write('Educational materials integrating various media elements such as text, images, audio, and video to provide a comprehensive learning experience.')

st.subheader('Real Object Model')
st.write('Physical models or real-world objects used in education to illustrate concepts, structures, or systems in a tangible and interactive manner.')

st.subheader('Slide Presentation')
st.write('A visual presentation created using software like PowerPoint or Google Slides, typically consisting of slides containing information, images, and graphics to convey a message or lesson.')

st.subheader('Technology-Supported Learning Include Computer-Based Training Systems')
st.write('Learning systems or software utilizing technology, including computer-based programs or online platforms, to facilitate educational content delivery and assessment.')

st.subheader('Video')
st.write('Visual content that can include lectures, demonstrations, experiments, or educational content presented in a video format, allowing learners to visually grasp complex concepts.')


