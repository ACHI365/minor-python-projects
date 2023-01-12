class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        lst = []
        for album in self.__albums:
            lst = lst + album.getSongs()

        lst = lst + self.__singles

        return max(lst, key=lambda x: x.getLikes())

    def leastLikedSong(self):
        lst = []
        for album in self.__albums:
            lst = lst + album.getSongs()
        lst = lst + self.__singles

        return min(lst, key=lambda x: x.getLikes())

    def totalLikes(self):
        lst = []
        for album in self.__albums:
            lst = lst + album.getSongs()
        lst = lst + self.__singles

        count = 0
        for song in lst:
            count += song.getLikes()

        return count

    def __str__(self):
        return "Name:" + self.__firstName + " " + self.__lastName + \
               ",Birth year:" + str(self.__birthYear) + \
               ",Total likes:" + str(self.totalLikes())
