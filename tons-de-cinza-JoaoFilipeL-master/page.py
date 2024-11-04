import streamlit as st
from PIL import Image
import numpy as np

st.title("Tons de cinza 🖼️ ")
st.markdown("---")

uploaded_file = st.file_uploader("📁 Escolha uma imagem para começar", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    option = st.selectbox(
        "Selecione o tipo de imagem que deseja exibir:",
        ("Original", "Luminosidade Linear", "NTSC",)
    )

    if option == "Original":
        st.markdown("### **Imagem Original**")
        st.image(image, use_column_width=True, channels="RGB")
        on = st.toggle("Binarização")
        if on:
            threshold = st.slider("Escolha: ", 0, 255, 25)
            if uploaded_file is not None:
                img = Image.open(uploaded_file)
                img_array = np.array(img)
            img = np.mean(img_array, axis =2, dtype=int)
            img_threshold = img.copy()
            img_threshold[img_threshold > threshold] = 255
            img_threshold[img_threshold <= threshold] = 0
            st.image(img_threshold)
            pass

    elif option == "Luminosidade Linear":
        if len(img_array.shape) == 3:
            r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
            y_linear = (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)
            st.markdown("### **Luminosidade Linear**")
            st.image(y_linear, use_column_width=True)
        else:
            st.error("A imagem já está em tons de cinza.")

    elif option == "NTSC":
        if len(img_array.shape) == 3:
            r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
            y_prime = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
            st.markdown("### **NTSC**")
            st.image(y_prime, use_column_width=True)
        else:
            st.error("A imagem já está em tons de cinza.")

else:
    st.markdown("Utilize arquivos PNG, JPG ou JPEG de até 10 MB.")
