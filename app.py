import streamlit as st
import qrcode
import io
import random
import string
from PIL import Image

st.title("🎉 QRコード自動生成ツール")

# QRコードのデータ生成
def generate_qr():
    random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    qr = qrcode.make(random_data)

    # メモリ上に画像を保存
    img_io = io.BytesIO()
    qr.save(img_io, format="PNG")
    img_io.seek(0)

    return img_io, random_data

if st.button("QRコードを生成"):
    img_io, data = generate_qr()
    
    # QRコード画像を表示
    st.image(Image.open(img_io), caption="生成されたQRコード", use_column_width=True)
    
    # ダウンロードリンクを作成
    st.download_button(label="📥 QRコードをダウンロード", data=img_io, file_name="qr_code.png", mime="image/png")

