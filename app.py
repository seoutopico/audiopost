import streamlit as st
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
import os

# Función para extraer el contenido del artículo de blog
def get_blog_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Suponiendo que el contenido del artículo está en etiquetas <p>
        paragraphs = soup.find_all('p')
        content = ' '.join([p.text for p in paragraphs])
        return content
    except Exception as e:
        st.write(f"Error al obtener el contenido: {e}")
        return ""

# Aplicación Streamlit
def main():
    st.title('Conversor de Artículos de Blog a Audio')

    # Campo para ingresar la URL
    url = st.text_input('Ingrese la URL del artículo de blog:', '')

    if url:
        # Botón para extraer y convertir a audio
        if st.button('Convertir a Audio'):
            content = get_blog_content(url)
            if content:
                # Convertir contenido a audio
                tts = gTTS(text=content, lang='es')
                audio_file = 'temp_audio.mp3'
                tts.save(audio_file)
                
                # Reproducir el audio en Streamlit
                st.audio(audio_file, format='audio/mp3')
                
                # Opcional: eliminar el archivo de audio después de usarlo
                os.remove(audio_file)

if __name__ == '__main__':
    main()
