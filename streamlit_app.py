import streamlit as st
from pathlib import Path

def blogPath(path_str='blog'):
    main_path = Path(".").absolute()
    blog_path = main_path.joinpath(path_str)
    return blog_path

def showPic(file_str, pic_path_str='assets', pic_ext=['jpg', 'png']):
    fs = file_str.split('.')
    f_ext = fs[-1]
    if f_ext[:3].lower() in pic_ext:
        f = fs[0].split('[')
        blog_path = blogPath()
        pic_path = blog_path.joinpath(pic_path_str)
        fn = f[-1]+'.'+f_ext[:3]
        fn = pic_path.joinpath(fn).absolute()
        if fn.is_file():
            st.image(str(fn))
        else:
            st.write(f"{fn} is not in {pic_path_str}")
    else:
        st.write(f"{fs} is not a picture name")

# Create a sidebar menu with different options
menu = ["Home", "List Posts", "Show MD", "Latex Example"]
choice = st.sidebar.selectbox("Menu", menu)

# Display the selected option
if choice == "Home":
    st.title("Hi. It's YK.")
    st.write("Welcome to my note space.")
    st.write("This is a simple blog app built with streamlit and python.")
    st.write("Enjoy!")

elif choice == "List Posts":
    st.title("List Posts")
    blog_path = blogPath()
    md_files = list(blog_path.glob('*.md'))
    for blog_file in md_files:
        with open(str(blog_file), 'r') as f:
            markdown_string = f.read()
        st.write(blog_file)

elif choice == "Show MD":
    st.title("Show MD")
    blog_path = blogPath()
    blog_file = blog_path.joinpath('Channel Method'+'.md').absolute()
    with open(str(blog_file), 'r') as f:
        markdown_string = f.read()
    md_s = markdown_string.split('\n')
    is_block = False
    for m_s in md_s:
        if len(m_s)>0:
            if m_s[0] in ['!']:
                showPic(m_s)
            elif m_s[0] in ['`']:
                is_block = not(is_block)
                if is_block:
                    block_s = f"{m_s}\n"
                else:
                    block_s += f"{m_s}"
                    st.markdown(block_s)
            elif is_block:
                block_s += f"{m_s}\n"
            else:
                st.markdown(m_s)
        elif is_block:
            block_s += f"{m_s}\n"
        else:
            st.markdown('\n')
    
elif choice == "Latex Example":
    st.title("Latex Example")
    st.markdown("The :orange[Valuation] **Frame**: PB.ROE.")
    st.markdown(r'''
            $$P_{t}=B_{t}\cdot(\frac{P}{B})_{t} $$
            ''')
    st.markdown(r'''
            $$\Delta P_{t} = \Delta B_{t}\cdot(\frac{P}{B})_{t} + B_{t}\cdot\Delta(\frac{P}{B})_{t} + \Delta B_{t}\cdot\Delta(\frac{P}{B})_{t}$$
            ''')
