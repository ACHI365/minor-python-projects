class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def notSameSong(self, compare_song):
        for song in self.__songs:
            if song.getTitle() == compare_song.getTitle() and \
                    song.getReleaseYear() == compare_song.getReleaseYear() and \
                    song.getDuration() == compare_song.getDuration():
                return False
        return True

    def addSongs(self, *songs):
        count = 0
        for song in songs:
            if self.notSameSong(song):
                self.__songs.append(song)
                count += 1
        return count

    def addSongs_aux(self, songs):
        for song in songs:
            if self.notSameSong(song):
                self.__songs.append(song)

    def sortBy(self, byKey, reverse):
        return sorted(self.__songs, key=byKey, reverse=reverse)

    def sortByName(self, reverse):
        return self.sortBy(byKey=lambda x: x.getTitle(), reverse=reverse)

    def sortByPopularity(self, reverse):
        return self.sortBy(byKey=lambda x: x.getLikes(), reverse=reverse)

    def sortByDuration(self, reverse):
        return self.sortBy(byKey=lambda x: x.getDuration(), reverse=reverse)

    def TotalLikes(self):
        count = 0
        for song in self.__songs:
            count += song.getLikes()
        return count

    def __str__(self):
        return "Title:" + self.__title + ",Release year:" + str(self.__releaseYear) \
               + ",songs:" + "{" + '|'.join([str(song) for song in self.__songs]) + "}"
