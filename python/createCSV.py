import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from os import system, name
import csv

# This version of the spotify playlist scanner just takes a value from the sys.arg and searches for the term
# spotify:user:1251475457
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def exitProgram():
    print("Thank you for using Spotipy Playlist Scanner")
    exit()

def printTracks(tracks, pId, pName):
    for i, item in enumerate(tracks['items']):
        global tempIndex
        global spamwriter
        global totalTracks
        global searchQuery
        tempIndex += 1
        track = item['track']
        try:
            print("|{}|\t<<{}/{}>>".format(searchQuery,tempIndex,totalTracks))
            trackWriter.writerow([ str(removeEmojis(track['name'])), str(track["id"]), str(pId), str(pName), str(track['explicit']), str(track['album']['release_date']), str(track['duration_ms']) ])
            # listOfTracks.append(Track( ))
        except:
            global mistakes
            mistakes+=1
            print("<<{}>> TRACK NOT ADDED".format(tempIndex))
        clear()

def removeEmojis(arg):
    return (str((arg).encode('utf-8', 'ignore')))[1:]

mistakes = 0
fileName = ""
listOfPlaylists = []
listOfTracks = []

class Playlist(object):
    def __init__(self, name=None, uri=None, uURI=None, total=None, image=None):
        self.name = name
        self.uri = uri
        self.uURI = uURI
        self.total = total
        self.image = image

class Track(object):
    def __init__(self, name=None, uri=None, pURI=None, pName=None, explicit=None, releaseDate=None, duration=None):
        self.name = name
        self.uri = uri
        self.pURI = pURI
        self.pName = pName
        self.explicit = explicit
        self.releaseDate = releaseDate
        self.duration = duration

# Get username from terminal
username = sys.argv[1]
try:
    searchQuery = ' '.join(sys.argv[2:])
except:
    print("No search term given")
    input()
    exitProgram()
# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

# Search for playlist
searchResults = spotifyObject.search(searchQuery,50,0,"playlist")
if searchResults['playlists']['total'] == 0:
    print("Sorry, that value did not return any playlists.")
    input()
    exitProgram()
searchResults2 = spotifyObject.search(searchQuery,50,50,"playlist")
playlists = searchResults['playlists']['items']
playlists += searchResults2['playlists']['items']
totalPlaylists = 0
totalTracks = 0

for item in playlists:
    totalPlaylists+=1
    totalTracks += item["tracks"]["total"]

index = 0
for item in playlists :
    index+=1
    listOfPlaylists.append(Playlist(removeEmojis(item['name']), item['uri'], item['owner']['id'], item['tracks']['total'], item['images'][0]['url']))

tempIndex = 0
fileName = searchQuery.replace(' ', '') + '.csv'
with open(fileName, mode='w') as trackWriter:
    trackWriter = csv.writer(trackWriter, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    newIndex = 0
    trackWriter.writerow(['track', 'track id', 'playlist id', 'playlist name', 'explicit', 'release date', 'duration'])
    for playlist in listOfPlaylists:
        try:
            results = spotifyObject.user_playlist(playlist.uURI, playlist.uri, fields="tracks, next")
            tracks = results['tracks']
            printTracks(tracks, playlist.uri, playlist.name)
            while tracks['next']:
                tracks = spotifyObject.next(tracks)
                printTracks(tracks, playlist.uri, playlist.name)
        except:
            mistakes+=1
            print("ISSUE")

fileName2 = searchQuery.replace(' ', '') + '_data.csv'
with open(fileName, mode='w') as trackWriter:
    trackWriter = csv.writer(trackWriter, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    newIndex = 0
    trackWriter.writerow(['track', 'track id', 'playlist id', 'playlist name', 'explicit', 'release date', 'duration'])
    for playlist in listOfPlaylists:
        try:
            results = spotifyObject.user_playlist(playlist.uURI, playlist.uri, fields="tracks, next")
            tracks = results['tracks']
            printTracks(tracks, playlist.uri, playlist.name)
            while tracks['next']:
                tracks = spotifyObject.next(tracks)
                printTracks(tracks, playlist.uri, playlist.name)
        except:
            mistakes+=1
            print("ISSUE")        
print("Number of mistakes: " + str(mistakes))
input("DONE")
