import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx

# 두 수를 더합니다.
result = 10 + 20

if get_script_run_ctx(suppress_warning=True) is None:
    # python app11.py 로 실행하면 터미널에 결과를 출력합니다.
    print(f"10 + 20 = {result}")
else:
    # streamlit run app11.py 로 실행하면 웹 화면에 결과를 표시합니다.
    st.title("간단한 덧셈 계산")
    st.write(f"10 + 20 = {result}")
