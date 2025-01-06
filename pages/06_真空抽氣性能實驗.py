import streamlit as st
import os

st.title("實驗六: 真空抽氣性能實驗")

st.write("這裡是真空抽氣性能實驗的詳細內容。")

file_path = "files/實驗6.真空抽氣性能實驗.xls"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()

    st.download_button(
        label="下載 實驗6.真空抽氣性能實驗.xls", 
        data=file_content,  
        file_name="實驗6.真空抽氣性能實驗.xls", 
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.error(f"檔案 {file_path} 不存在！")

# 在這裡添加實驗一的具體內容，如圖表、數據等
