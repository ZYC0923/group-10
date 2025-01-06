import streamlit as st
import os

st.title("實驗四: 管路摩擦與閥特性實驗")

st.write("這裡是管路摩擦與閥特性實驗的詳細內容。")

# 設定文件路徑
file_paths = {
    "docx": "files/實驗4.黏滯係數量測.docx",
    "pdf": "files/實驗4.黏滯係數量測.pdf",
    "xls": "files/實驗4.黏滯係數量測.xlsx"
}

# 檢查文件並提供下載按鈕
for file_type, path in file_paths.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            file_content = f.read()

        # 根據不同的文件類型設定 MIME 類型
        if file_type == "docx":
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            label = "下載 實驗4.黏滯係數量測.docx"
        elif file_type == "pdf":
            mime_type = "application/pdf"
            label = "下載 實驗4.黏滯係數量測.pdf"
        elif file_type == "xls":
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            label = "下載 實驗4.黏滯係數量測.xlsx"

        # 顯示下載按鈕
        st.download_button(
            label=label, 
            data=file_content,  
            file_name=path.split("/")[-1], 
            mime=mime_type
        )
    else:
        st.error(f"檔案 {path} 不存在！")

# 在這裡添加實驗一的具體內容，如圖表、數據等