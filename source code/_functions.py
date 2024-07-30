import librosa
import numpy as np
import pandas as pd
from scipy.stats import mode
import os
from matplotlib import pyplot as plt

def frame_audio_signal(signal, frame_lenght=13000, hop_lenght=500) -> list:
    frames = []
    for i in range(0, len(signal) - frame_lenght + 1, hop_lenght):
        frames.append(signal[i:i + frame_lenght])
    return frames

# all the frames extracted from the same audio file will have the same sample rate
def mfcc_features_extract(frames, sample_rate, n_mfcc=13) -> np.array:
    mfcc_features = []
    for frame in frames:
        mfcc = np.mean(
            librosa.feature.mfcc(
                y=frame,
                sr=sample_rate,
                n_mfcc=n_mfcc
            ).T,
            axis=0
        )
        mfcc_features.append(mfcc)
    return np.array(mfcc_features) # return a array with 13 values

def load_data(root_path):
    data = []
    for folder in os.listdir(root_path):
        label = folder
        #print(1)
        for file in os.listdir(root_path + '/' + folder):
            # audio path
            #print(2)
            if file.endswith('.wav'):
                file_path = os.path.join(root_path + '/' + folder + '/' + file)
                data.append(
                    {
                        'path': file_path,
                        'label': label
                    }
                )
    return data

# Function to filter valuable frames based on frequencies
# def filter_mfcc_features_by_frequency(mfcc_features, frequency_threshold=2):
#     filtered_mfcc_features = []
#     variances = [np.var(mfcc) for mfcc in mfcc_features]
#     # Calculate frequency of variance values for each MFCC feature
#     frequencies = np.sum([variances], axis=0)  # Assuming variance values are non-negative
#     # print(frequencies)
#     # print(f'{len(frequencies)},{len(mfcc_features)}')
#     # Iterate through MFCC features and filter based on frequency threshold
#     for i, feature in enumerate(mfcc_features):
#         print(f'{i},{feature}')
#         if frequencies[i] >= frequency_threshold:
#             filtered_mfcc_features.append(feature)
#     return np.array(filtered_mfcc_features)

import numpy as np

def filter_mfcc_features_by_frequency(mfcc_features, threshold=5):
    # Calculate the variance for each frame across all MFCC features
    frame_variances = np.var(mfcc_features, axis=1)
    # Determine the range of variances and divide into 50 equal-width bins
    min_value = np.min(frame_variances)
    max_value = np.max(frame_variances)
    bin_edges = np.linspace(min_value, max_value, num=51)  # 50 bins -> 51 edges
    
    # Count the frequency of frame variances in each bin
    frequencies, _ = np.histogram(frame_variances, bins=bin_edges)
    
    # Identify bins with frequencies below the threshold
    low_freq_bins = np.where(frequencies < threshold)[0]
    
    # Filter out frames that fall into low frequency bins
    keep_indices = []
    for i, variance in enumerate(frame_variances):
        bin_index = np.digitize(variance, bins=bin_edges) - 1
        if bin_index not in low_freq_bins:
            keep_indices.append(i)
    # Select the frames to keep
    filtered_mfcc_features = mfcc_features[keep_indices]
    
    return filtered_mfcc_features

# Example usage:
# Assuming 'mfcc_features' is a 2D NumPy array with shape (num_frames, num_features)
# filtered_mfcc_features = filter_mfcc_features_by_frequency(mfcc_features, threshold=5)


# audio = '_test/neutral/neutral_normal_dogs_10.wav'
# signal, sample_rate = librosa.load(audio, sr=None)
# frames = []
# frame_size = 13000
# hop_size = 500
# for i in range(0, len(signal)-frame_size+1, hop_size):
#     frame = signal[i: i+frame_size]
#     # plt.figure(figsize=(15, 5))
#     # librosa.display.waveshow(frame, sr=sample_rate)
#     # plt.show()
#     frames.append(frame)

# Function to visualize variance distribution
def visualize_variance_distribution(mfcc_features):
    variances = [np.var(mfcc) for mfcc in mfcc_features]
    plt.hist(variances, bins=50)
    plt.xlabel('Variance')
    plt.ylabel('Frequency')
    plt.title('Distribution of MFCC Variance')
    plt.show()