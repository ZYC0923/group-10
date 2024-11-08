import streamlit as st
import os
from PIL import Image

st.title("實驗三: 柏努利文氏管實驗")

st.write("這裡是柏努利文氏管實驗的詳細內容。")

file_path = "files/伯努利文氏管實驗.docx"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()

    st.download_button(
        label="下載 柏努利文氏管實驗.docx", 
        data=file_content,  
        file_name="伯努利文氏管實驗.docx", 
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.error(f"檔案 {file_path} 不存在！")

image = Image.open('picture/1.png')
st.image(image, caption='圖片1')
image = Image.open('picture/1.png')
st.image(image, caption='圖片2')
image = Image.open('picture/3.png')
st.image(image, caption='圖片3')
image = Image.open('picture/4.png')
st.image(image, caption='圖片4')
image = Image.open('picture/5.png')
st.image(image, caption='圖片5')
# 在這裡添加實驗一的具體內容，如圖表、數據等
