from album import Album
from artist import Artist
from song import Song


class SpotiPy:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def notSameArtist(self, compare_artist):
        for artist in self.__artists:
            if artist.getFirstName() == compare_artist.getFirstName() and \
                    artist.getSecondName() == compare_artist.getSecondName() and \
                    artist.getBirthYear() == compare_artist.getBirthYear():
                return False
        return True

    def addArtists(self, *artistas):
        for artist in artistas:
            if self.notSameArtist(artist):
                self.__artists.append(artist)

    def addArtists_aux(self, artistas):
        for artist in artistas:
            if self.notSameArtist(artist):
                self.__artists.append(artist)

    def getTopTrendingArtist(self):
        singer = None
        maximum = -1

        for artist in self.__artists:
            if artist.totalLikes() > maximum:
                maximum = artist.totalLikes()
                singer = artist

        return singer.getFirstName(), singer.getSecondName()

    def getTopTrendingAlbum(self):
        albums = []
        for artist in self.__artists:
            albums += artist.getAlbums()

        best_album = None
        maximum = -1

        for album in albums:
            if album.TotalLikes() > maximum:
                best_album = album
                maximum = album.TotalLikes()

        return best_album.getTitle()

    def getTopTrendingSong(self):
        allSongs = []

        for artist in self.__artists:
            for album in artist.getAlbums():
                allSongs += album.getSongs()
            allSongs += artist.getSingle()

        return (max(allSongs, key=lambda x: x.getLikes())).getTitle()

    @staticmethod
    def loadFromFile(path):
        spotipy = SpotiPy()

        with open(path, "r") as file:
            data = file.read()  # read all chars
            data = data[data.find("{") + 1:].strip()  # start after artists:{
            artists = []  # create artists list
            while data.strip()[0] != '}' and len(data) > 0:
                if len(artists) == 0:
                    artist = data[0:data.find("albums:")].strip().strip(
                        ',')  # distinguish artist -> from start to albums

                    artist = artist.split(',')
                elif data.find("#") > -1:
                    artist = data[data.find("#") + 1:data.find("albums")].strip().strip(',')

                    artist = artist.split(',')
                else:
                    break

                album_index = data.find("albums:")  # get album-index

                data = data[
                       data.find('{', album_index) + 1:].strip()  # update data according to our current location
                albums = []
                singles = []
                while data.strip()[0] != '}':
                    if len(albums) == 0:
                        album_initials = data[0:data.find("songs:")].strip().strip(',')
                        album_initials = album_initials.split(",")

                        albums.append(Album(album_initials[0].strip(),
                                            int(album_initials[
                                                    1].strip())))  # detect album name and release year, then create
                    else:
                        next_album = data.find('%', 0, data.find("singles"))
                        album_initials = data[next_album + 1:data.find("songs:")].strip().strip(',')
                        album_initials = album_initials.split(",")
                        albums.append(Album(album_initials[0].strip(),
                                            int(album_initials[
                                                    1].strip())))

                    song_index = data.find("songs:")

                    data = data[data.find('{', song_index) + 1:].strip()  # update data

                    songs = []  # create song list

                    while data.strip()[0] != '}':  # while paragraph is not finish do the following
                        next_song = data.find("|", 0, data.find(
                            "}"))  # if next song exists then find by |, else use brackets
                        if next_song > -1:
                            song = data[0:next_song].strip()  # distinguish song
                            data = data[data.find('|') + 1:].strip()
                            if song[0] == '{':
                                song = song[1:].strip()
                            song = song.split(",")
                            songs.append(
                                Song(song[0].strip(), int(song[2].strip()),
                                     int(float(song[1].strip("minutes").strip()) * 60),
                                     int(song[3].strip())))
                        else:
                            song = data[0:data.find('}')].strip()  # distinguish song
                            if not song == "{":
                                if song[0] == '{':
                                    song = song[1:].strip()
                                song = song.split(",")
                                songs.append(
                                    Song(song[0].strip(), int(song[2].strip()),
                                         int(float(song[1].strip("minutes").strip()) * 60),
                                         int(song[3].strip())))
                            data = data[data.find('}'):].strip()

                    data = data.strip()[1:]
                    albums[len(albums) - 1].addSongs_aux(songs)

                data = data.strip()[1:]
                single_index = data.find("singles")

                data = data[
                       data.find('{', single_index):].strip()

                while data.strip()[0] != '}':
                    next_song = data.find("|", 0, data.find(
                        "}"))  # if next song exists then find by |, else use brackets
                    if next_song > -1:
                        song = data[0:next_song].strip()  # distinguish song
                        data = data[data.find('|') + 1:].strip()
                        if song[0] == '{':
                            song = song[1:].strip()
                        song = song.split(",")
                        singles.append(
                            Song(song[0].strip(), int(song[2].strip()),
                                 int(float(song[1].strip("minutes").strip()) * 60),
                                 int(song[3].strip())))
                    else:
                        song = data[0:data.find('}')].strip()  # distinguish song
                        if not song == "{":
                            if song[0] == '{':
                                song = song[1:].strip()
                            song = song.split(",")
                            singles.append(
                                Song(song[0].strip(), int(song[2].strip()),
                                     int(float(song[1].strip("minutes").strip()) * 60),
                                     int(song[3].strip())))
                        data = data[data.find('}'):].strip()

                data = data.strip()[1:].strip()
                artists.append(Artist(artist[0], artist[1], int(artist[2]), albums, singles))

            spotipy.addArtists_aux(artists)
            return spotipy


if __name__ == '__main__':
    rattlestarSong = Song('Snake Jazz', 1989)
    majorSong = Song('Space Oddity', 1969, 315)
    queenSong = Song('Teo Torriatte', 1977, 355, 132178)

    snakeJazz = Song('Snake Jazz', 1989)

    greenSide = Album("Green side", 1976)
    print(greenSide.getTitle())
    print(greenSide)

    print(greenSide.addSongs(snakeJazz))
    print(greenSide)

    print(greenSide.addSongs(snakeJazz, majorSong))
    print(greenSide)

    print(greenSide.addSongs(snakeJazz, snakeJazz,  queenSong, rattlestarSong))
    print(greenSide)


    print(snakeJazz.getReleaseYear())  # 1989

    # By default, likes are 0, it increases by 1 when `like()` is called
    print(snakeJazz.getLikes())  # 0
    print(snakeJazz.like())
    print(snakeJazz.getLikes())  # 1

    # Duration is 60 by default
    print(snakeJazz.getDuration())  # 60
    print(snakeJazz.setDuration(90))
    print(snakeJazz.getDuration())  # 90

    path1 = "data/data0.txt"
    path2 = "data/data1.txt"

    spotipy1 = SpotiPy.loadFromFile(path1)
    artist = spotipy1.getArtists()[1]
    print(artist.getSingle()[1])
    print(artist.getAlbums()[0])
    print(spotipy1.getArtists()[0].mostLikedSong())

    print(spotipy1.getTopTrendingAlbum())

    spotipy2 = SpotiPy.loadFromFile(path2)
    artist = spotipy2.getArtists()[0]
    print(artist.getSingle()[0])
    print(artist.getAlbums()[0])

    print(spotipy2.getTopTrendingSong())