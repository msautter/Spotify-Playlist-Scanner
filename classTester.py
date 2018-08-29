class Playlist(object):
    def __init__(self, name=None, URI=None, uURI=None, total=None):
        self.name = name
        self.URI = URI
        self.uURI = uURI
        self.total = total
    def __str__(self):
        return(" Name: {} \n URI: {} \n User: {} \n Total: {}")


listOfPlaylists = []

listOfPlaylists.append(Playlist("Playlist Name1", "1rtp95Qy9pKB34uWWai2ta", "gidget53", 4356))
listOfPlaylists.append(Playlist("Playlist Name2", "2rtp95Qy9pKB34uWWai2ta", "gidget54", 990))
listOfPlaylists.append(Playlist("Playlist Name3", "3rtp95Qy9pKB34uWWai2ta", "gidget55", 8))
listOfPlaylists.append(Playlist("Playlist Name4", "4rtp95Qy9pKB34uWWai2ta", "gidget56", 76))
listOfPlaylists.append(Playlist("Playlist Name5", "5rtp95Qy9pKB34uWWai2ta", "gidget57", 4456))


for item in listOfPlaylists:
    print(str(item.name))