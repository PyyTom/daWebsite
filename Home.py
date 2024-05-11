import streamlit as st,base64,glob
from streamlit_extras.app_logo import add_logo
from PIL import Image
icon=Image.open('images/tl.png')
st.set_page_config(page_title='PyTom',page_icon=icon,layout='wide')
add_logo('images/tl.png')
images=glob.glob('images/contacts/0*.*')
links = ['https://www.facebook.com/tommaso.latorre/', 'https://www.linkedin.com/in/tomas-la-torre-a95672253/',
         'https://www.instagram.com/tommy.latorre/', 'https://stackoverflow.com/users/14641703/tommy','https://github.com/PyyTom', ]
col_a,col_b=st.columns([1,1])
with col_a:
    st.markdown('''<style>.stApp{{background-image:url(data:image/jpeg;base64,{});background-size:cover;}}</style>'''.format(base64.b64encode(open('images/bg/bg.jpeg','rb').read()).decode()),unsafe_allow_html=True)
    st.subheader("Hi, :wave: I am Tommy from Valencia, ES :es:\nHere's my stuff")
with col_b:
    col_0, col_1, col_2, col_3, col_4, col_5, col_6 = st.columns([1, 1, 1, 1, 1, 1, 1])
    cols = [col_0, col_1, col_2, col_3, col_4]
    for n in range(len(images)):
        with cols[n]:
            st.markdown("""<a href={}><img src="data:image/png;base64,{}" width="75"></a>""".format(links[n],base64.b64encode(open(images[n],"rb").read()).decode()),unsafe_allow_html=True, )
    with col_5:
        st.markdown(
            """<a href='mailto:tommaso_latorre@hotmail.com'><img src="data:image/png;base64,{}" width="75"></a>""".format(
                base64.b64encode(open('images/contacts/mail.png', "rb").read()).decode()), unsafe_allow_html=True, )
    with col_6:
        st.markdown("""<a href='https://wa.me/34603206204'><img src="data:image/png;base64,{}" width="75"></a>""".format(
            base64.b64encode(open('images/contacts/phone.png', "rb").read()).decode()), unsafe_allow_html=True, )
with st.sidebar:
    st.sidebar.image('images/tl.png')