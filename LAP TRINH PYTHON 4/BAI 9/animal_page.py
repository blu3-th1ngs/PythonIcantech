import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([2, 1])

with col1:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con khỉ')
with col4:
    b4 = st.button('Đại bàng')
with col5:
    b5 = st.button('Con gà')

if b1:
    with col6:
        st.write('Âm thanh')
        audio = open('BAI 9/cat-meow-401729.mp3', 'rb')
        st.audio(audio, format='audio/mp3')
        st.write('Video')
        video = 'https://www.youtube.com/watch?v=W86cTIoMv2U'
        st.video(video, format='video/mp4')
    with col7:
        image = 'BAI 9/cat.jfif'
        st.image(image, caption='Con mèo')

if b2:
    with col6:
        st.write('Âm thanh')
        audio = open('BAI 9/free-dog-bark-419014.mp3', 'rb')
        st.audio(audio, format='audio/mp3')
        st.write('Video')
        video = 'https://www.youtube.com/watch?v=zb9l63Nm9zU'
        st.video(video, format='video/mp4')
    with col7:
        image = 'BAI 9/dog.jfif'
        st.image(image, caption='Con chó')

if b3:
    with col6:
        st.write('Âm thanh')
        audio = open('BAI 9/monkey-128368.mp3', 'rb')
        st.audio(audio, format='audio/mp3')
        st.write('Video')
        video = 'https://www.youtube.com/watch?v=icd_ob8UWgQ'
        st.video(video, format='video/mp4')
    with col7:
        image = 'BAI 9/monkey.jfif'
        st.image(image, caption='Con khỉ')

if b4:
    with col6:
        st.write('Âm thanh')
        audio = open('BAI 9/eagle-281163.mp3', 'rb')
        st.audio(audio, format='audio/mp3')
        st.write('Video')
        video = 'https://www.youtube.com/watch?v=1ryv1u2yXCk'
        st.video(video, format='video/mp4')
    with col7:
        image = 'BAI 9/eagle.jfif'
        st.image(image, caption='Đại bàng')

if b5:
    with col6:
        st.write('Âm thanh')
        audio = open('BAI 9/chicken-cluking-type-3-293320.mp3', 'rb')
        st.audio(audio, format='audio/mp3')
        st.write('Video')
        video = 'https://youtu.be/SNSr8ti3Y4A'
        st.video(video, format='video/mp4')
    with col7:
        image = 'BAI 9/chicken.jfif'
        st.image(image, caption='Con gà')