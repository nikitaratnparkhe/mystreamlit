import streamlit as st
st.set_page_config(page_title='Mystreamlit',page_icon='shark')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Download'))
st.image('https://onleitechnologies.in/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1-144x81.png')
st.title('Onlei Technology')
st.header('By Nikita')
st.text('This is a tutorial on streamlit library')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=OSnHZDZoQv8')
elif (mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter name')
        DOB=st.date_input("Choose Date of Birth")
        marks=st.slider('Choose marks')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name=',name,'DOB:',DOB,'Marks:',marks)
elif (mymenu=='Download'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt')
