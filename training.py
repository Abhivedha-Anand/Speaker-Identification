import numpy as np
from sklearn.mixture import GaussianMixture
import librosa
import os
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Function to extract MFCC features from an audio file
def extract_features(audio_file):
    y, sr = libr-osa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return mfccs.T

# Directory containing audio files for each speaker
data_dir ='/content/drive/My Drive/Sem 6/ML Mini Project/Training Data'
audio_files = os.listdir(data_dir)

# Prepare features and labels
all_features = []
labels = []
for i, audio_file in enumerate(audio_files):
    audio_path = os.path.join(data_dir, audio_file)
    features = extract_features(audio_path)
    all_features.append(features)
    labels.extend([i] * len(features))

# Convert to numpy arrays
all_features = np.vstack(all_features)
labels = np.array(labels)

# Train a GMM for each speaker
num_speakers = len(audio_files)
gmm_models = []
for speaker_id in range(num_speakers):
    speaker_features = all_features[labels == speaker_id]
    gmm = GaussianMixture(n_components=2, random_state=0)  # You can experiment with the number of components
    gmm.fit(speaker_features)
    gmm_models.append(gmm)

