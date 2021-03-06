import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from os import system, name
import csv


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
        global trackWriter
        tempIndex += 1
        track = item['track']
        try:
            print("<<{}>> {}, {}, {}, {}".format(tempIndex, removeEmojis(track['artists'][0]['name']), removeEmojis(track['name']), pId, pName))
            trackWriter.writerow([ str(removeEmojis(track['name'])), str(track["id"]), str(pId), str(pName), int(track['explicit']), str(track['album']['release_date']), str(track['duration_ms']) ])
            if str(removeEmojis(track['id'])) in hashTable:
                hashTable[str(removeEmojis(track['id']))] = hashTable[str(removeEmojis(track['id']))].value()+1
            else:
                hashTable[str(removeEmojis(track['id']))] = 0
        except:
            global mistakes
            mistakes+=1
            print("<<{}>> TRACK NOT ADDED --------------------------------------".format(tempIndex))

def removeEmojis(arg):
    return (str((arg).encode('utf-8', 'ignore')))[1:]

mistakes = 0
fileName = ""
listOfPlaylists = []
listOfTracks = []
hashTable = {}

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
# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']

clear()
print("Welcome! " + displayName)
print("Followers: " + str(followers))
# Search for playlist
searchQuery = input("Search Word: ")
print()
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

print("Your search term, \'{}\', returned {} tracks across {} playlists".format(searchQuery, totalTracks, totalPlaylists))

choice = input("Would you like to print playlists? (y/n)")
if choice == 'y':
    index = 0
    for item in playlists :
        index+=1
        print(">>> PLAYLIST: " + str(index))
        print("       PNAME:        " + removeEmojis(item['name']))
        print("         PID:        " + item["uri"])
        print("       COUNT:        " + str(item["tracks"]["total"]))
        listOfPlaylists.append(Playlist(removeEmojis(item['name']), item['uri'], item['owner']['id'], item['tracks']['total'], item['images'][0]['url']))
    input("Press any key to continue...")
    clear()

print("   Search Term: " + searchQuery)
print("   Track Count: " + str(totalTracks))
print("Playlist Count: " + str(totalPlaylists))

input("Press any key to continue...")
clear()
tempIndex = 0

choice = input("Would you like to print tracks to a file? (y/n)")
if choice == 'y':
    fileName = input("What would you like to name the file (.csv)? ")
    if fileName == '':
        fileName = searchQuery.replace(" ", "-")
        fileName += "-uncompressed"
        print(fileName)
    if fileName[-4:] != '.csv':
        fileName += '.csv'
    with open(fileName, mode='w') as trackWriter:
        trackWriter = csv.writer(trackWriter, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        newIndex = 0
        trackWriter.writerow(['track', 'track id', 'playlist id', 'playlist name', 'explicit', 'release date', 'duration'])
        for playlist in listOfPlaylists:
            results = spotifyObject.user_playlist(playlist.uURI, playlist.uri, fields="tracks, next")
            tracks = results['tracks']
            printTracks(tracks, playlist.uri, playlist.name)
            while tracks['next']:
                tracks = spotifyObject.next(tracks)
                printTracks(tracks, playlist.uri, playlist.name)

choice = input("Would you like to print the hash table?")
print(hashTable)

if choice == 'n':
    input("Thank you for using the Spotify Playlist Scanner CLI")
    exitProgram()
input("Number of mistakes: " + str(mistakes))
exitProgram()
        # print (str(playlist['name']))
        # print ('total tracks: ' + str(playlist['tracks']['total']))
        # results = spotifyObject.user_playlist()
