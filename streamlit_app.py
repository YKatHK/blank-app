import streamlit as st
from pathlib import Path
from datetime import datetime

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

def showBlog(md_file):
    with open(str(md_file), 'r') as f:
        markdown_string = f.read()
    md_s = markdown_string.split('\n')
    is_block = False
    for m_s in md_s[1:]: # the 1st line of MD is Date
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

def sortBlogList(md_files):
    kv = {}
    for md_file in md_files:
        with open(str(md_file), 'r') as f:
            file_date = f.readline()
        kv[md_file] = datetime.strptime(file_date.strip("\n"), '%Y.%m.%d')
    kv_sorted = sorted(kv.items(), key=lambda d: d[1], reverse=True)
    return [k for (k,v) in kv_sorted]

def showBlogList(blogs_path='blog'):
    blog_path = blogPath(path_str=blogs_path)
    md_files = list(blog_path.glob('*.md'))
    md_files = sortBlogList(md_files)
    for md_file in md_files:
        md_file_str = md_file.stem
        st.subheader(md_file_str)
        with open(str(md_file), 'r') as f:
            file_date = f.readline()
        with st.expander(f":gray[{file_date}]"):
            showBlog(md_file)

tab1, tab2, tab3 = st.tabs(["Home", "Blogs", "About Me"])

with tab1:
    st.header("About This App")
    st.write("Hi. It's YK.")
    st.write("Welcome to my note space.")
    st.write("This is a simple blog app built with streamlit and python.")

with tab2:
    #st.header("Blogs")
    showBlogList()
    #md_head = 'Channel Method'
    #md_file = 'Channel Method'+'.md'
    #showBlog(md_head, md_file)

with tab3:
    st.header("About Me")
