from tqdm import tqdm
import librosa
import numpy as np
from python_speech_features import mfcc

# Returns male and female voices
def load_audio(audio_files):
	# Allocate empty list for male and female voices
    male_voices = []
    female_voices = []

    for file in tqdm(audio_files):
        if file.startswith('wavs/male-'):
            male_voices.append(librosa.load(file))
        elif file.startswith('wavs/female-'):
            female_voices.append(librosa.load(file))

	# Convert the list into Numpy array
    male_voices = np.array(male_voices, dtype=object)
    female_voices = np.array(female_voices, dtype=object)

    return male_voices, female_voices

# The function to extract audio features
def extract_features(audio_data):

	# Remember that the audio data consists of raw audio wave followed by sample rate
	# so we need to only take the raw audio wave.
	audio_waves = audio_data[:,0]
	samplerate = audio_data[:,1][0]

	features = []
	for audio_wave in tqdm(audio_waves):
		features.append(mfcc(audio_wave, samplerate=samplerate, numcep=26, nfft=1103))

	features = np.array(features, dtype=object)
	return features

# The function used to concatenate all audio features forming a long 2-dimensional array
def concatenate_features(audio_features):
    concatenated = audio_features[0]
    for audio_feature in tqdm(audio_features):
        concatenated = np.vstack((concatenated, audio_feature))

    return concatenated
