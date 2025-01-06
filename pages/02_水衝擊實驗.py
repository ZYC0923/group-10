import streamlit as st
import os
import fitz  # PyMuPDF
from PIL import Image
import io

st.title("實驗二: 水衝擊實驗")

st.write("這裡是水衝擊實驗的詳細內容。")

# 設定文件路徑
file_paths = {
    "pdf": "files/實驗2.水衝擊實驗.pdf",  # 水衝擊實驗 PDF
    "docx": "files/實驗2.水衝擊實驗.docx",  # 水衝擊實驗 DOCX
    "xls": "files/實驗2.水衝擊實驗.xls"  # 水衝擊實驗 Excel 文件
}

# 顯示下載按鈕在頁面上方
for file_type, path in file_paths.items():
    if os.path.exists(path):  # 檢查文件是否存在
        with open(path, "rb") as f:
            file_content = f.read()

        # 根據不同的文件類型設定 MIME 類型
        if file_type == "pdf":
            mime_type = "application/pdf"
            label = "下載 實驗2.水衝擊實驗.pdf"
        elif file_type == "docx":
            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            label = "下載 實驗2.水衝擊實驗.docx"
        elif file_type == "xls":
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            label = "下載 實驗2.水衝擊實驗.xls"

        # 顯示下載按鈕
        st.download_button(
            label=label,
            data=file_content,
            file_name=path.split("/")[-1],
            mime=mime_type
        )
    else:
        st.error(f"檔案 {path} 不存在！")

# 顯示 PDF 文件的內容並提取圖片
if "pdf" in file_paths and os.path.exists(file_paths["pdf"]):
    st.subheader("實驗2: 水衝擊實驗.pdf 內容")
    pdf_path = file_paths["pdf"]

    # 打開 PDF 文件
    doc = fitz.open(pdf_path)

    # 設定圖片編號
    image_counter = 1  # 用於圖片編號

    # 顯示每頁的文本內容
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # 加載頁面

        # 提取文本
        page_text = page.get_text("text")

        # 顯示頁面的文本內容
        st.text(page_text)

        # 提取每頁圖片的尺寸
        image_list = page.get_images(full=True)  # 提取圖片
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]  # 圖片數據
            image = Image.open(io.BytesIO(image_bytes))  # 打開圖片

            # 方法 2：將圖片處理成較小的格式保存
            st.subheader(f"圖片 {image_counter}")
            max_width, max_height = 800, 600
            image.thumbnail((max_width, max_height))  # 縮小圖片
            temp_image_path = f"temp_image_{image_counter}.png"
            image.save(temp_image_path, "PNG")  # 保存圖片
            st.image(temp_image_path, caption=f"圖片 {image_counter}")  # 顯示圖片

            # 更新圖片編號
            image_counter += 1
