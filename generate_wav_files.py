import pandas as pd
from tqdm import tqdm
from pydub import AudioSegment

# Load the csv file into data frame
df = pd.read_csv('archive/cv-valid-train.csv')

# Create two new data frames
df_male = df[df['gender']=='male']
df_female = df[df['gender']=='female']

# Find out the number of rows
print(df_male.shape)		# output: (55029, 8)
print(df_female.shape)		# output: (18249, 8)

# Take only 300 male and 300 female data
df_male = df_male[:300]
df_female = df_female[:300]

# Define the audio path
TRAIN_PATH = 'archive/cv-valid-train/'

# The function to convert mp3 to wav
def convert_to_wav(df, m_f, path=TRAIN_PATH):
    for file in tqdm(df['filename']):
        sound = AudioSegment.from_mp3(path+file)

		# Create new wav files based on existing mp3 files
        if m_f == 'male':
            sound.export('wavs/male-'+file.split('/')[-1].split('.')[0]+'.wav', format='wav')
        elif m_f == 'female':
            sound.export('wavs/female-'+file.split('/')[-1].split('.')[0]+'.wav', format='wav')

    return

# How to use the convert_to_wav() function
convert_to_wav(df_male, m_f='male')
convert_to_wav(df_female, m_f='female')
