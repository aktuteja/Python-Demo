import pandas as pd
import matplotlib as mp
from matplotlib import pyplot as plt

#Read a CSV file as a dataframe
data = pd.read_csv("SpotifyTopPlaylist.csv")
#print(data)
print(data.head())
print(data.info())

artists = data['artists'].unique()
no_of_artists = data['artists'].nunique()
print("Artists in trending list: ", no_of_artists)
#print(artists)

#plt.plot(data.artists, data.liveness)
#plt.show()

