import streamlit as st

st.title("實驗三: 柏努利文氏管實驗")

st.write("這裡是柏努利文氏管實驗的詳細內容。")

file_paths = {
    "doc": "file/伯努利文氏管實驗.docx",
}
def create_download_button(file_path, label, mime_type):
    with open(file_path, "rb") as f:
        file_content = f.read()
    st.download_button(
        label=label,
        data=file_content,
        file_name=file_path.split("/")[-1],  # 檔案名稱
        mime=mime_type
    )
# 在這裡添加實驗一的具體內容，如圖表、數據等
