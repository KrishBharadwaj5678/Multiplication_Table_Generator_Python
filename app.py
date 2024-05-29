import streamlit as st

st.title(":blue[Multiplication Table Generator]")

# Taking user Input

num=st.number_input(":orange[Enter a Number]",1)

times=st.number_input(":orange[Enter Number of Times]",1)

# Generate Button

generate=st.button(":green[Generate]")

if generate:
    for i in range(1,times+1):
        st.write(f"<h2 style='color: lightblue;text-align:center;text-shadow:0px 0px 15px lightblue;'>{num} * {i} = {num*i}</h2>",unsafe_allow_html=True)