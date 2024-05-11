import streamlit as st,glob,base64
from PIL import Image
icon=Image.open('images/tl.png')
st.set_page_config(page_title='PyTom - Software',page_icon=icon,layout='wide')
st.title('SOFTWARE')
st.markdown('''<style>.stApp{{background-image:url(data:image/jpeg;base64,{});background-size:cover;}}</style>'''.format(
        base64.b64encode(open('images/bg/bg_software.jpeg', 'rb').read()).decode()), unsafe_allow_html=True)
titles=[(folder.split('/')[-2]).split('-')[0] for folder in glob.glob('/Users/tommylatorre/Applications/Products/2_Software/**/')]
technologies=[folder.split('-')[1][:-1] for folder in glob.glob('/Users/tommylatorre/Applications/Products/2_Software/**/')]
previews=[preview for preview in glob.glob('/Users/tommylatorre/Applications/Products/2_Software/**/*.png')]
descriptions=[]
for folder in glob.glob('/Users/tommylatorre/Applications/Products/2_Software/**/'):
    readme=open(folder+'/readme.txt','r')
    description=readme.read()
    descriptions.append(description)
    readme.close()
for n in range(len(titles)):
    c_image,c_data=st.columns([1,1])
    with c_image:st.image(previews[n], width=500)
    with c_data:st.text_area(value=titles[n]+'\n\nTECHNOLOGY:\n'+technologies[n]+'\n\nDESCRIPTION:\n'+descriptions[n],label='',height=250,disabled=True)
