The provided Python code is designed to analyze a set of songs, extracting information about the instruments used in each track and visualizing the duration of a specific instrument over time. The code employs the Essentia library for audio analysis, focusing on pitch and instrumentalness features.

Function extract_instruments:

Takes the path to an audio file as input.
Loads the audio file using Essentia's MonoLoader.
Extracts the predominant pitch and confidence using PredominantPitchMelodia.
Segments the pitch into notes using PitchContourSegmentation.
Estimates the instrumentalness of the audio using Instrumentalness.
Creates a DataFrame with time, note, and instrumentalness information.
Function plot_instrument_duration:

Takes the DataFrame produced by extract_instruments and the name of a specific instrument (e.g., 'Piano') as input.
Filters the data for the specified instrument.
Plots the instrumentalness of the instrument over time using Matplotlib.
Example Usage:

Demonstrates how to use the functions with a sample audio file path.
Calls extract_instruments to obtain a DataFrame with instrumentalness information.
Calls plot_instrument_duration to visualize the instrumentalness of a specific instrument ('Piano') over time.
Dependencies:

Requires the Essentia library for audio processing. Install it using pip install essentia.
Note:

The accuracy of instrument extraction depends on the quality of the audio file and the complexity of the music. Fine-tuning of parameters may be necessary for different use cases.
Visualization:

The code generates a line plot showing the instrumentalness of a specific instrument over time, providing insights into the presence and duration of the instrument in the analyzed audio track.
