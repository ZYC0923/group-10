import streamlit as st
import os
from PIL import Image

st.title("實驗三: 柏努利文氏管實驗")

st.write("這裡是柏努利文氏管實驗的詳細內容。")

file_paths = {
    "docx": "files/實驗3.伯努利文氏管實驗.docx",
    "pdf": "files/實驗3.伯努利文氏管實驗.pdf"
}

# 檢查文件並提供下載按鈕
for file_type, path in file_paths.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            file_content = f.read()

        # 根據不同的文件類型設定 MIME 類型
        if file_type == "docx":
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            label = "下載 實驗3.伯努利文氏管實驗.docx"
        elif file_type == "pdf":
            mime_type = "application/pdf"
            label = "下載 實驗3.伯努利文氏管實驗.pdf"

        # 顯示下載按鈕
        st.download_button(
            label=label, 
            data=file_content,  
            file_name=path.split("/")[-1], 
            mime=mime_type
        )
    else:
        st.error(f"檔案 {path} 不存在！")

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

