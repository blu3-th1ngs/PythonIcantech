import streamlit as st

bill = {}

with st.form('Order đồ uống'):
    drinks = ('Trà sữa truyền thống', 'Trà sữa matcha', 'Trà sữa trái cây', 'Trà sữa socola', 'Trà sữa khoai môn', 'Trà sữa oolong')
    option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)
    
    sugars = ('Đường trắng', 'Đường nâu', 'Ít đường', 'Không đường')
    option_sugar = st.selectbox('Bạn thích thêm loại đường nào?', sugars)
    
    jellys = ('Thạch rau câu', 'Thạch nha đam', 'Trân châu trắng', 'Trân châu đen', 'Thạch café', 'Không thêm thạch')
    option_jelly = st.selectbox('Bạn thích thêm loại thạch nào?', jellys)
    
    sizes = ('Nhỏ', 'Vừa', 'Lớn', 'Đại')
    option_size = st.selectbox('Bạn muốn size nào?', sizes)
    
    toppings = ('Không thêm topping', 'Kem cheese', 'Kem trứng', 'Đậu đỏ', 'Thạch phô mai')
    option_topping = st.selectbox('Bạn muốn thêm topping gì?', toppings)
    
    ice_options = ('Nhiều đá', 'Ít đá', 'Không đá', 'Đá riêng')
    option_ice = st.selectbox('Bạn muốn đá như thế nào?', ice_options)
    
    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 1)
    
    submitted = st.form_submit_button("Xác nhận")

if submitted:
    bill = {
        'Loại đồ uống:': option_drink,
        'Loại đường:': option_sugar,
        'Loại thạch:': option_jelly,
        'Size:': option_size,
        'Topping:': option_topping,
        'Đá:': option_ice,
        'Số lượng:': nums
    }
    
    st.write('Bạn đã chọn:')
    for x, y in bill.items():
        st.write(x, y)
    
    if bill:
        ans = ''
        for x in bill:
            ans += str(x) + ' ' + str(bill[x]) + '\n'
        
        st.download_button(
            label='Tải hoá đơn',
            data=ans,
            file_name='hoa_don.txt',
            mime='text/plain'
        )