import requests
from bs4 import BeautifulSoup

def get_song_list(url):
    # Send a GET request to the Setlist.fm URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the song names in the page
    # Songs are typically in a list, adjust the selector if needed
    songs = soup.select('.setlistParts .songLabel')  # CSS selector for song labels
    song_list = [song.text.strip() for song in songs]
    
    return song_list

# URL of the Setlist.fm page
url = "https://www.setlist.fm/setlist/the-offspring/2024/forum-theatre-melbourne-australia-3557d1f.html"

# Get the song list and print it
song_list = get_song_list(url)
if song_list:
    print("Songs in the setlist:")
    for idx, song in enumerate(song_list, start=1):
        print(f"{idx}. {song}")
else:
    print("No songs found or an error occurred.")
