# Proyecto inteligencia Artificial 1
## Integrantes: Miguel Brito, José I. Escudero
## Tema: Reconocimiento de genero mediante voz

Este proyecto asume que se esta usando Python 3.11.2


### Instrucciones para ejecutar el proyecto
1. Instalar FFMPEG y agregarlo al PATH
2. Descargar datos de entrenamiento: https://www.kaggle.com/datasets/mozillaorg/common-voice (Almacenar en carpeta llamada `archive`. Son 13.56 GB)
3. Establezca un entorno virtual si aún no lo ha hecho: `python -m venv .venv`
4. Iniciar entorno virtual: `source .venv/bin/activate`
5. Instalar dependencias: `pip install -r requirements.txt`
6. Ejecutar `python generate_wav_files.py` para convertir los archivos de Kaggle a formato WAV.
7. Abrir los distintos jupyter notebooks y ejecutar sus celdas.
