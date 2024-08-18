import streamlit as st

st.title("Hi. It's YK.")
st.write(
    "Welcome to my note space."
)

st.markdown("The :orange[Valuation] **Frame**: PB.ROE.")

st.markdown(r'''
        P_{t}=B_{t}\cdot(\frac{P}{B})_{t} 
        ''')

st.markdown(r'''
        $$\Delta P_{t} = \Delta B_{t}\cdot(\frac{P}{B})_{t} + B_{t}\cdot\Delta(\frac{P}{B})_{t} + \Delta B_{t}\cdot\Delta(\frac{P}{B})_{t}$$
        ''')
