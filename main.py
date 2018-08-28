import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from os import system, name

# print(json.dumps(searchResults, sort_keys=True, indent=4))
# spotify:user:1251475457

def printPlaylists(playlists) :
    # clear()
    index = 0
    for item in playlists:
        index+=1
        print(">>> PLAYLIST: " + str(index))
        print("       PNAME:        " + item["name"])
        print("         PID:        " + item["uri"])
        print("       COUNT:        " + str(item["tracks"]["total"]))
    input("Press any key to continue...")
    
def playlistMenu(playlists, searchTerm, tPlaylists, tTracks):
    while True:
        #clear()
        print()
        print(">>> Playlist Menu <<<")
        print("       KEYWORD: " + searchTerm)
        print("PLAYLIST COUNT: " + str(tPlaylists))
        print("   TRACK COUNT: " + str(tTracks))
        print("What would you like to do with these playlists?")
        print("4 - Run Data Analysis on these playlists")
        print("3 - Print Playlists to file")
        print("2 - Print Playlists to console")
        print("1 - Exit")
        choice = input("\t\tYour choice: ")
        if choice == "4":
            playlistDataAnalysis(playlists, tPlaylists, tTracks)
        if choice == "3":
            print("COMING SOON")
        if choice == "2":
            printPlaylists(playlists)
        if choice == "1":
            exitProgram()

def playlistDataAnalysis(playlists, tPlaylists, tTracks):
    playlistIndex = 0
    trackIndex = 0
    for item in playlists:
        playlistIndex +=1
        # print("Playlist: " + item['name'])
        # print(str(playlistIndex) + "/" + str(tPlaylists) + "playlists")
        trackRequest = spotifyObject.user_playlist_tracks(item['owner']['id'], playlist_id=item['id'], fields=None, limit=100, offset=0, market=None)
        tracks = trackRequest['items']
        for track in tracks:
            clear()
            trackIndex+=1
            print(str(trackIndex) + "/" + str(tTracks) + " tracks")
            # print(track['track']['name'])
            f = open("demofile.txt", "a")
            try: 
                print((str(track["track"]["name"]) + ", " + str(track["track"]["album"]["artists"][0]["name"])).encode('utf8'))
            except:
                print("Shit's fucked yo")
            # f.write("\n" + str(track["track"]["name"]) + "," + str(track["track"]["album"]["artists"][0]["name"]))
        #print(json.dumps(tracks, sort_keys=True, indent=4))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def exitProgram() :
    print("Thank you for using Spotipy Playlist Scanner")
    exit()

# ////////START OF PROGRAM//////////


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

while True:
    #clear()
    print("Welcome! " + displayName)
    print("Followers: " + str(followers))
    print()
    print(">>> MAIN MENU <<<")
    print()
    print("2 - Playlist Scanner")
    print("1 - Exit")
    choice = input("\t\tYour choice: ")
    # Search for playlist
    if choice == "2":
        searchQuery = input("\t\tKeyword: ")
        print()
        searchResults = spotifyObject.search(searchQuery,50,0,"playlist")
        if searchResults['playlists']['total'] == 0:
            print("Sorry, that value did not return any playlists. Please try again")
        else:
            searchResults2 = spotifyObject.search(searchQuery,50,50,"playlist")
            playlists = searchResults['playlists']['items']
            playlists += searchResults2['playlists']['items']
            index = 0
            total = 0
            for item in playlists:
                index+=1
                total += item["tracks"]["total"]
            playlistMenu(playlists, searchQuery, index, total)
    if choice == "1":
        exitProgram()

