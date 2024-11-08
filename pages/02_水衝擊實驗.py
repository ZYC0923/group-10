import streamlit as st
import os

st.title("實驗二: 水衝擊實驗")

st.write("這裡是水衝擊實驗的詳細內容")

file_path = "files/實驗2.水衝擊實驗.docx"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()

    st.download_button(
        label="下載 實驗2.水衝擊實驗.docx", 
        data=file_content,  
        file_name="實驗2.水衝擊實驗.docx", 
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.error(f"檔案 {file_path} 不存在！")

# 在這裡添加實驗一的具體內容，如圖表、數據等