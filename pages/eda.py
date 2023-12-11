import streamlit as st

def col_17px_text(text):
    color = "#0091D5"
    font_size = "17px"
    bold = True
    italic = True
    style = "font-size:{}; color:{}; font-weight:bold; font-style:italic;" if bold else "font-size:{}; color:{};"
    return f"<span style='{style.format(font_size, color)}'>{text}</span>"

st.title('Exploratory Data Analysis (EDA)', anchor=False)

intro_eda = f"""
<div style="text-align: justify;">
    <p>The data is collected via a {col_17px_text('survey')} using a Google form. It is distributed across students in Universiti Malaya. The collected dataset consists of data from years {col_17px_text('2021 to 2023')}. It consists of {col_17px_text('1035 rows')} and {col_17px_text('47 columns')} comprising of demographics (3), preferred learning mode (1), learning objects preferrences (13) and the VAK learning style questions (30).</p>
</div>


"""
st.markdown(intro_eda, unsafe_allow_html=True)

tableau_embeded = """
<div class='tableauPlaceholder' id='viz1702043538136' style='position: relative'><noscript><a href='#'><img alt='Dataset Distribution Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSPDashboards&#47;DatasetDistributionDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DSPDashboards&#47;DatasetDistributionDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSPDashboards&#47;DatasetDistributionDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1702043538136');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(tableau_embeded, height=550)

tableau_embeded_lo = """
<div class='tableauPlaceholder' id='viz1702043645760' style='position: relative'><noscript><a href='#'><img alt='Most Preferred Learning Objects Based on a Dominant VAK Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LO&#47;LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LO&#47;LODashboard&#47;MostPreferredLearningObjectsBasedonaDominantVAKDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1702043645760');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""
st.components.v1.html(tableau_embeded_lo, height=550)