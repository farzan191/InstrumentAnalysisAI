import essentia.standard as ess
import pandas as pd
import matplotlib.pyplot as plt

def extract_instruments(audio_path):
    # Load audio file
    loader = ess.MonoLoader(filename=audio_path)
    audio = loader()

    # Extract the predominant melody
    melody_extractor = ess.PredominantPitchMelodia()
    pitch, pitch_confidence = melody_extractor(audio)

    # Extract the predominant melody's notes
    note_extractor = ess.PitchContourSegmentation()
    note_segments, _ = note_extractor(pitch, pitch_confidence)

    # Extract the dominant instrument
    instrument_extractor = ess.Instrumentalness()
    instrument_prob = instrument_extractor(audio)

    # Create a DataFrame with extracted information
    df = pd.DataFrame({'Time': note_segments[:, 0], 'Note': note_segments[:, 1], 'Instrumentalness': instrument_prob})
    df['Time'] = df['Time'] * 1000  # Convert time to milliseconds

    return df

def plot_instrument_duration(df, instrument_name):
    # Filter data for the specified instrument
    instrument_data = df[df['Note'] == instrument_name]

    # Plot the instrumentalness over time
    plt.plot(instrument_data['Time'], instrument_data['Instrumentalness'], label=instrument_name)
    plt.xlabel('Time (ms)')
    plt.ylabel('Instrumentalness')
    plt.title(f'Instrumentalness of {instrument_name} over Time')
    plt.legend()
    plt.show()

# Example usage
audio_file_path = 'path/to/your/audio/file.mp3'
df = extract_instruments(audio_file_path)

# Plot the duration of a specific instrument (e.g., 'Piano')
plot_instrument_duration(df, 'Piano')
