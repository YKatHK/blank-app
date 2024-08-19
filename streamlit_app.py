import streamlit as st

st.title("Hi. It's YK.")
st.write(
    "Welcome to my note space."
)

st.markdown("The :orange[Valuation] **Frame**: PB.ROE.")

st.markdown(r'''
        $$P_{t}=B_{t}\cdot(\frac{P}{B})_{t} $$
        ''')

st.markdown(r'''
        $$\Delta P_{t} = \Delta B_{t}\cdot(\frac{P}{B})_{t} + B_{t}\cdot\Delta(\frac{P}{B})_{t} + \Delta B_{t}\cdot\Delta(\frac{P}{B})_{t}$$
        ''')

# Create a sidebar menu with different options
menu = ["Home", "View Posts"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected option
if choice == "Home":
    st.title("Welcome to my blog")
    st.write("This is a simple blog app built with streamlit and python.")
    st.write("Enjoy!")

elif choice == "View Posts":
    st.title("View Posts")
    with open('blog\Beijing Hutongs.md', 'r') as f:
        markdown_string = f.read()
    st.markdown(markdown_string)
