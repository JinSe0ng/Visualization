import streamlit as st
import pandas as pd

# 웹 제목 설정
st.title('첫 번째 streamlit 앱')

# 텍스트 출력
st.write('안녕하세요! strealit 입니다.')

# 데이터 프레임 출력
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [30, 25, 22]} 
df = pd.DataFrame(data)

# 데이터 프레임 출력
st.dataframe(df)

# 막대 그래프 생성
st.bar_chart(df['age'])
