This project assumes you are using python 3.11.2
1. Install FFMPEG and add to PATH
2. Download train data: https://www.kaggle.com/datasets/mozillaorg/common-voice (Set it in a folder called `Archive`)
3. Set virtual environment if you haven't already: python -m venv .venv
4. Start virtual environment: `source .venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Execute `python generate_wav_files.py` to generate the wav files
7. Open any jupyter notebook and run the cells
