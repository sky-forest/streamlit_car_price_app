import streamlit as st

def run_home_app():
    st.text('이 앱은 데이터 분석 및 데이터 예측에 사용됩니다.')
    st.text('고객 정보를 넣으면 얼마정도의 차를 구매할지를 예측해준다.')
   
    img_url= 'https://img.hankyung.com/photo/202205/AA.30080001.1.jpg'
    st.image(img_url)
