def identify_speaker_from_drive(audio_file_path, gmm_models):
    # Extract features from the new sample
    features = extract_features(audio_file_path)

    # Calculate likelihoods for each speaker using the trained GMM models
    likelihoods = []
    for gmm in gmm_models:
        likelihood = np.sum(gmm.score(features))
        likelihoods.append(likelihood)

    # Identify the speaker with the highest likelihood
    predicted_speaker = np.argmax(likelihoods)

    return predicted_speaker

# Path to the new audio file on Google Drive
new_audio_file_path = '/content/drive/My Drive/Sem 6/ML Mini Project/Testing Data/Predicted Labels/Harini.mp4'

# Identify the speaker of the new audio file using the trained GMM models
predicted_speaker_id = identify_speaker_from_drive(new_audio_file_path, gmm_models)
print(predicted_speaker_id)

if predicted_speaker_id==0:
  print("Unknown Speaker")

else:

  # Map the predicted speaker ID to the corresponding speaker name
  predicted_speaker_name = audio_files[predicted_speaker_id]

  print("Predicted Speaker:", predicted_speaker_name)
