import streamlit as st

# Defining Page Title,Icon
st.set_page_config(
    page_title="Multiplication Table Generator",
    page_icon="🧠",
    menu_items={
        "About":"Our Multiplication Table Generator is designed to assist users in creating customized multiplication tables effortlessly."
    }
)

st.markdown(" ### :orange[Welcome to our Multiplication Table Generator.]")

st.write("<h5>Whether you're a student sharpening your math skills or a teacher preparing lesson materials, our user-friendly tool makes it easy to generate custom multiplication tables.</h5>",unsafe_allow_html=True)


# Taking user Input

num=st.number_input(":orange[Enter a Number]",1)

times=st.number_input(":orange[Enter Number of Times]",1)

# Generate Button

generate=st.button(":green[Generate]")

if generate:
    for i in range(1,times+1):
        st.write(f"<h2 style='color: lightblue;text-align:center;text-shadow:0px 0px 15px lightblue;'>{num} * {i} = {num*i}</h2>",unsafe_allow_html=True)
