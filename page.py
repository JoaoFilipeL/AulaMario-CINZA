import streamlit as st
from PIL import Image
import numpy as np

st.title("Tons de cinza 🖼️ ")
st.markdown("---")

uploaded_file = st.sidebar.file_uploader("Escolha um arquivo", type=['png', 'jpg', 'jpeg'])
st.sidebar.write("Utilize arquivos PNG, JPG ou JPEG.")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    option = st.selectbox(
        "Selecione o tipo de imagem que deseja exibir:",
        ("Original","Cinza","Luminosidade Linear", "NTSC","Binarização")
    )

    if option == "Original":
        if uploaded_file is not None:
            st.image(uploaded_file, caption='Imagem original') 

    elif option == "Cinza":
       if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img_array = np.array(img)
        img_cinza_mean = np.mean(img_array, axis=2, dtype=int)
        st.image(img_cinza_mean, caption='Imagem em tons de cinza (médias)')

    elif option == "Luminosidade Linear":
        if uploaded_file is not None:
            r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
            img_l = (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)
            st.image(img_l, caption='Imagem em tons de cinza (Luminosidade Linear)')
        else:
            st.error("A imagem já está em tons de cinza.")

    elif option == "NTSC":
        if uploaded_file is not None:
            r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
            img_n = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
            st.image(img_n, caption='Imagem em tons de cinza (NTSC)')
        else:
            st.error("A imagem já está em tons de cinza.")

    elif option == "Binarização":
        
        escolha = st.radio(
            ["Imagem Colorida", "Imagem cinza"] 
    )
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
  
