import streamlit as st
import os

st.title("實驗四: 管路摩擦與閥特性實驗")

st.write("這裡是管路摩擦與閥特性實驗的詳細內容。")

file_path = "files/實驗4.黏滯係數量測.xlsx"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()

    st.download_button(
        label="下載 實驗4.黏滯係數量測.xlsx", 
        data=file_content,  
        file_name="實驗4.黏滯係數量測.xlsx", 
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.error(f"檔案 {file_path} 不存在！")

# 在這裡添加實驗一的具體內容，如圖表、數據等
