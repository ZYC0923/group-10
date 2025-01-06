import streamlit as st
import os

st.title("實驗六: 真空抽氣性能實驗")

st.write("這裡是真空抽氣性能實驗的詳細內容。")

# 設定文件路徑
file_paths = {
    "docx": "files/實驗6.真空抽氣性能實驗.docx",
    "pdf": "files/實驗6.真空抽氣性能實驗.pdf",
    "xls": "files/實驗6.真空抽氣性能實驗.xls"
}

# 檢查文件並提供下載按鈕
for file_type, path in file_paths.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            file_content = f.read()

        # 根據不同的文件類型設定 MIME 類型
        if file_type == "docx":
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            label = "下載 實驗6.真空抽氣性能實驗.docx"
        elif file_type == "pdf":
            mime_type = "application/pdf"
            label = "下載 實驗6.真空抽氣性能實驗.pdf"
        elif file_type == "xls":
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            label = "下載 實驗6.真空抽氣性能實驗.xls"

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