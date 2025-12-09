import streamlit as st

with st.sidebar:
    image = 'images.webp'
    st.image(image, caption='Harry Styles')
    
    st.write('Họ và tên: Harry Edward Styles')
    st.write('Nghệ danh: Harry Styles')
    
    st.write('Harry Edward Styles là một ca sĩ, nhạc sĩ và diễn viên người Anh. Anh bắt đầu sự nghiệp âm nhạc với tư cách là thành viên của nhóm nhạc One Direction, sau đó phát hành album solo đầu tay vào năm 2017. Styles được biết đến với phong cách âm nhạc đa dạng và thời trang độc đáo, giành nhiều giải thưởng quan trọng bao gồm Grammy Awards và BRIT Awards.')

st.title('Bài hát yêu thích')
st.write('As It Was')
audio_file = open('asitwas.mp3', 'rb')
st.audio(audio_file, format='audio/mp3')

st.title('MV yêu thích')
st.write('As It Was - Official Video')
video_url = 'https://www.youtube.com/watch?v=H5v3kku4y6Q'
st.video(video_url)