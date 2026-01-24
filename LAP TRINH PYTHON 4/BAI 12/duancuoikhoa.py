import streamlit as st

st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')

with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến Vương quốc mô hình!')
    st.image('anh/download.jpg')
    st.write('Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. Luôn cập nhật và đa dạng sản phẩm. Cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!')
    st.write(':house: Địa chỉ cửa hàng: Tòa 25T2, Nguyễn Thị Thập, Trung Hoà, Cầu Giấy, Hà Nội')
    st.write(':phone: Điện thoại liên hệ: 0123-456-789')

st.title('Vương quốc mô hình')
col1, col2, col3 = st.columns(3)

with col1:
    b1 = st.button('Dragon Ball')
with col2:
    b2 = st.button('Naruto')
with col3:
    b3 = st.button('One Piece')

if b1:
    st.header('Danh sách mô hình Dragon Ball')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('anh/goku.jpg', caption='Goku Ultra Instinct - Mã số: 001')
    with col5:
        st.image('anh/vegeta.jpg', caption='Vegeta Super Saiyan - Mã số: 002')
    with col6:
        st.image('anh/picolo.jpg', caption='Picolo - Mã số: 003')

if b2:
    st.header('Danh sách mô hình Naruto')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('anh/naruto.jpg', caption='Uzumaki Naruto - Mã số: 001')
    with col5:
        st.image('anh/sasuke.jpg', caption='Uchiha Sasuke - Mã số: 002')
    with col6:
        st.image('anh/kakashi.jpg', caption='Hatake Kakashi - Mã số: 003')

if b3:
    st.header('Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('anh/luffy.jpg', caption='Monkey D. Luffy - Mã số: 001')
    with col5:
        st.image('anh/zoro.jpg', caption='Roronoa Zoro - Mã số: 002')
    with col6:
        st.image('anh/sanji.jpg', caption='Vimsmoke Sanji - Mã số: 003')

st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):
    topics = ('Dragon Ball', 'Naruto', 'One Piece')
    option_topic = st.selectbox('Chủ đề mô hình', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('Mã số mô hình', codes)

    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)

    name = st.text_input('Họ và tên')

    phone = st.text_input('Số điện thoại liên hệ')

    address = st.text_input('Địa chỉ giao hàng')

    submitted = st.form_submit_button("Xác nhận đặt hàng")

if submitted:
    st.header('Bạn đã chọn:')
    
    bill = {'Loại mô hình': option_topic, 'Mã số': option_code, 'Số lượng': nums,
            'Họ tên khách hàng': name, 'Số điện thoại liên hệ': phone, 'Địa chỉ giao hàng': address}
    
    for x, y in bill.items():
        st.write(f'**{x}:** {y}')

    ans = '=== HÓA ĐƠN MUA HÀNG ===\n\n'
    for x in bill:
        ans += f'{x}: {bill[x]}\n'
    ans += '\n=== CẢM ƠN QUÝ KHÁCH ==='
    
    st.download_button('📥 Tải hóa đơn', ans, file_name='hoa_don.txt', mime='text/plain')