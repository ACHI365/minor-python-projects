# SpotiPy

In this homework, you should create a simple song manager program - SpotiPy. It can be used to store data about songs, albums, and artists, and update it according to users activities.

In this task you have to implement several classes - `Song`, `Album`, `Artist` and `SpotiPy`. Each of them is responsible for storing and/or manading a particular part of the data.

*All of the classes mentioned below,should be implemented in seperate .py file. All of  the files should be named same as the class contained in it.
Ex.: `song.py` file should contain `Song` class.*

## Song

At first, you should implement `Song` class, as song is the smallest data entity in our software. Each song should be described with following attributes:
* `title` - Title
* `releaseYear` - Release year
* `duration` - Duration in seconds
* `likes` - Amount of likes (Just a number, measuring the popularity)

All 4 attributes should be hidden (private) and should have getter methods (`getTitle`, `getReleaseYear`, `getDuration`, `getLikes`). Also, you should implement a constroctor to create `Song` objects. In the constructor set 60 as a default value for the duration of the song and 0 for the likes.

**Example**

~~~Python
#All 3 are valid examples of creating a song:
rattlestarSong = Song('Snake Jazz', 1989)
majorSong = Song('Space Oddity', 1969, 315)
queenSong = Song('Teo Torriatte', 1977, 355, 132178)
~~~

Since some songs can be cropped or extended,you have to provide setter function for *duration* attribute as well, which returns false if the given parameter is less than 0, more than 720 or same as it was before. Otherwise, it should return true and set duration attribute equal to a new value.

Instead of creating a single setter method, you should create `like()` and `unlike()` methods to manage the changes in song's popularity. When called `like()` should increase `likes` amount by 1 and `unlike()` should decrease it by 1.


~~~Python
snakeJazz = Song('Snake Jazz', 1989)

snakeJazz.getReleaseYear() # 1989

# By default, likes are 0, it increases by 1 when `like()` is called
snakeJazz.getLikes() # 0 
snakeJazz.like()
snakeJazz.getLikes() # 1

# Duration is 60 by default
snakeJazz.getDuration() # 60
snakeJazz.setDuration(90)
snakeJazz.getDuration() # 90
~~~

The `__str__` method is one of special methods in Python, like `__init__`. In short, `__str__` function is used to change how an object looks like when converted to string. For example, when printing (`print(song)`) or converting it to string (`str(song)`) (You can read more about it [here](https://www.pythontutorial.net/python-oop/python-__str__/)). Your `__str__` function should represent the song in the following format: "Title:{title},Duration:{duration(but converted into minutes)},Release year:{releaseYear},Likes:{likes}". See an example bellow.

**Example**
~~~Python
>>> snakeJazz = Song('Snake Jazz', 1989, 30)
>>> print(snakeJazz)
Title:Snake Jazz,Duration:0.5 minutes,Release year:1989,Likes:0
~~~
Note that the duration time is converted in minutes (30 -> 0.5). You should follow the exact format. There should not be extra whitespaces or other symbols in the string.

## Album

Next, you should create a class **Album** to store the collection of songs in one object. The albums should have the following attributes: 

* `title` - Title
* `releaseYear` - The Year it was released
* `songs` - A collection of songs, represented as a list of `Song` objects.

All 3 attributes should be hidden (private) and should have getter methods (`getTitle`, `getReleaseYear`, `getSongs`).

The `Album` class should have a constructor that takes title and release year as arguments and initializes appropriate attributes. The song list should be initialized with an empty list.

Also you should create a method  `addSongs()` which takes arbitrary many songs as a parameter and adds them to the album, only if the album does not contain the same songs. At the end, the method should return a single integer - how many new songs were added to the album.

Two songs are consider to be the same if they have exact same title, release year and duration. For example, these 3 songs are considered to be same - `Song('My Song', 2011, 120, 1570)`, `Song('My Song', 2011, 120, 1570)`, `Song('My Song', 2011, 120, 7500)` . While these 3 are different from each other - `Song('My Song', 2011, 120, 450)`, `Song('Other Song', 2011, 120, 150)`, `Song('My Song', 2011, 50, 450)`.

**Example**
~~~Python
>>> greenSide = Album("Green side",1976)
>>> greenSide.getTitle()
"Green side"
>>> # One song is added to the album
>>> greenSide.addSongs(snakeJazz)
1
>>> # 2 songs are provided, but one of them is already part of the album
>>> greenSide.addSongs(snakeJazz, majorSong)
1
>>> greenSide.addSongs(repeatedSong, newSong,  repeatedSong)
2
~~~

The main method of this class that you need to implement is `sortBy()`. You may have noticed that in lot's of music streaming platforms, you can sort the playlists/albums with duration, release year and etc. Our song manager software should provide similar service as well. `sortBy()` sorts the songs as specified bellow and returns sorted list of songs. It should take 2 arguments:
    * `byKey` - It is a function, that takes `Song` object as an argument and returns a key, that should be used to compare songs with when sorting.
    * `reverse` - It is a boolean which determines the order of the sorting. If true, songs should be sorted in ascending order. If false - descending order.
Python provides built-in sort methods that you can use (`sort`, `sorted`) or you can implement sorting algorithm on your own. More about sorting in python can be found [here](https://docs.python.org/3/howto/sorting.html).

You should create several more specific sorting methods as well - `sortByName()`, `sortByPopularity()`, `sortByDuration()`, `sortByReleaseYear()`. Each of these function takes a single boolean argument `reverse`, which specifies the sorting order, like in `sortBy()`. **Important**: this methods MUST call `sortBy` method with appropriate values, they should NOT do sorting by themself! In short main task of these functions is to provide `sortBy` with a proper `byKey` function.
* `sortByName(reverse)` - Returns the list of songs sorted alphabetically by their name (Ascending if 'reverse' is true, descending otherwise). These sort should not be case sensitive. For example, when sorting the strings - ['bc', 'Abc', 'abd', 'Bcd'] - in ascending order, disregarding the case, we get ['abc', 'abd', 'bc', 'bcd']. *Note: These method should return the list of song objects, not just their names.*
* `sortByPopularity(reverse)` - Returns the list of songs sorted by their popularity (Ascending if 'reverse' is true, descending otherwise).
* `sortByDuration(reverse)` - Returns the list of songs sorted by their duration (Ascending if 'reverse' is true, descending otherwise).
* `sortByReleaseYear(reverse)` - Returns the list of songs sorted by their release year (Ascending if 'reverse' is true, descending otherwise).


And lastly, for this class, implement a  *str()*  function, which just textual representation of the album in the following format - 'Title:{title},Release year:{release year},songs:{{song1}|{song2}|{song3}...}'. See examples for more details:

*Album with no songs:*
~~~Python
>>> greenSide = Album("Green side",1976)
>>> print(greenSide)
Title:Green side,Release year:1976,songs:{}
~~~

*Album with a single song:*
~~~Python
>>> snakeJazz = Song('Snake Jazz', 1989, 30)
>>>
>>> greenSide = Album("Green side",1976)
>>> greenSide.addSongs(snakeJazz)
>>> print(greenSide)
Title:Green side,Release year:1976,songs:{Title:Snake Jazz,Duration:0.5 minutes,Release year:1989,Likes:0}
~~~

*Album with multiple songs:*
~~~Python
>>> snakeJazz = Song('Snake Jazz', 1989, 30)
>>> majorSong = Song('Space Oddity', 1969, 60, 12000)
>>>
>>> greenSide = Album("Green side",1976)
>>> greenSide.addSongs(snakeJazz)
>>> print(greenSide)
Title:Green side,Release year:1976,songs:{Title:Snake Jazz,Duration:0.5 minutes,Release year:1989,Likes:0|Title:Space Oddity,Duration:1 minutes,Release year:1969,Likes:12000}
~~~

## Artist

The **Artist** is the last entity class to implement. The artist should have the following attributes: 

* `firstName` - A first name
* `lastName` - A last name
* `birthYear` - The year person was born in
* `albums` - The collection of albums, represented as a list of `Album` objects
* `singles` - The list of songs (That are not part of any albums and are released seperately), represeted as a list of `Song` objects.

All 5 attributes should be hidden (private) and should have getter methods (`getFirstName`, `getSecondName`, `getBirthYear`, `getAlbums`, `getSingle`).

Furthermore you should create a several methods in `Artist` class.

Create a method called `mostLikedSong()`,which will return the most liked song of the artist. *Note*: your function should compare all the songs from singles and all the albums.

Create a method called `leastLikedSong()` which behaves in the same way as `mostLikedSong()` method, but instead of the most popular song, it returns the least popular one.

Create a method `totalLikes()` which returns the total number of likes for this artist. Again, consider all songs from the albums and singles.

And at the end, `__str__()`  method should be implemented as well. It should return the following representation of the artist: 'Name: {firstName} {lastName},Birth year:{birthYear},Total likes:{total likes of this artist}'. *Note*: '{' and '}' are used to mark values and should not be part of the final output and string representation of the artist does not include albums and singles.


# SpotiPy

This is the final and the main class of this software - `SpotiPy`.

`SpotiPy` has a single hidden (private) attribute `artists` - a collection of artist, represented as a list of `Artist` objects. A constructor does not take any arguments and should initialize `artists` with an empty list.

Furthermore, `SpotiPy` should have following methods:
* `getArtists()` - Returns the list of of artists.
* `addArtists()` - Adds arbitrary many Artist objects to the list, if they are not already in the list. 2 `Artist` objects are considered to be the same, if they have the same first name, last name and birth year.
* `getTopTrendingArtist()` - Returns the tuple of the first name and the last name (`('john', 'doe')`) of the artist that has the most likes - sum of likes from all songs from all albums and singles.
* `getTopTrendingAlbum()` - Returns the name of the album with the most total likes - sum of like of all songs in this album. It should compare all albums in all artists.
* `getTopTrendingSong()` - Returns the name of the song with the most likes. It should consider all the songs in all artists albums or singles.
*Note: If there are several artists/albums/songs with same maximum amount of likes, return any of them.* 

The last function that you should implement, is a class (**static**) method, not casual method! The function, `loadFromFile()`, takes a string, path to the the file that contains the data. This static/class function should read data from the file, store it as a list of Artists, add them in the `SpotiPy` object and return it. In short, it creates a `SpotiPy` object from the file. How file looks like is described bellow.

You can find several data files included in this homework. Use them to test your solution.

### File format

The file contains a list of artists, which contains list of albums and a single. Each albums and singles contains the list of songs. All of those lists *can* be empty or contain a single or multiple elements.

The file starts with `artists:` writen and than in the brackates, `{}` is written a list of artists. Artists are seperated by `#` symbol.

Each **artist** is written in a following way: first name, comma - `,`, last name, comma - `,`, the year of birth, comma - `,` a word `albums:` and than a list of albums written in brackets - `{}`. Albums are seperated by `%`. After albums list closes with a bracket, we have a comma - `,`, a word `singles:` and a list of songs written in brackets - `{}`. Songs are seperated by `|` symbol.

Each **album** is written in a following way: name of the album, comma - `,`, the year of release, comma - `,`, a word `songs:` and the list of songs written in brackets `{}`. Songs are seperated by `|` symbol.

Each **song** is written in a following way: name, comma - `,`, time in minutes, a space ` ` and word `minutes`, comma `,`, the year of release, comma `,` and likes.

See bellow examples.

A song:
~~~txt
Each Panics,1.2 minutes,2005,175
~~~

An album:
~~~txt
Shortsighted Client,2018,songs:
{
     Each Panics,1.2 minutes,2005,175
    |Petri Stiller,0.5 minutes,2012,135
}
~~~

An artist:
~~~txt
Jarrett,Church,1981,
albums:
{
     Shortsighted Client,2018,songs:
    {
         Each Panics,1.2 minutes,2005,175
        |Petri Stiller,0.5 minutes,2012,135
    }
},
singles:
{
    Winer Retarder Florin,3.1 minutes,2018,109
}
~~~

An example complete file:
~~~txt
artists:
{
     Jarrett,Church,1981,
    albums:
    {
         Shortsighted Client,2018,songs:
        {
             Each Panics,1.2 minutes,2005,175
            |Petri Stiller,0.5 minutes,2012,135
        }
    },
    singles:
    {
        Winer Retarder Florin,3.1 minutes,2018,109
    }
    #Kaia,Joseph,1976,
    albums:
    {
         Biographies,1994,songs:
        {
            Would Gables,0.9 minutes,1999,78
        }
        %Tonnage,2021,songs:
        {
             Stairways Stamps,3.5 minutes,2003,16
            |Repertory Council,5.2 minutes,1998,45
            |Swing Trump,9.2 minutes,2006,129
        }
    },
    singles:
    {
         Pageantry Torpedoes,0.7 minutes,1990,147
        |Pestilent,0.0 minutes,2003,128
        |Repent Bum,3.8 minutes,2014,53
    }
}
~~~


**IMPORTANT**

You can assume that all names (artist's, song's, etc.) contains only spaces, upper case and lower case english letters. Years and likes are valid integers. Duration is a valid float. 

The data can be written on multiple lines and each line can start with prefix of whitespaces. That means, that all examples bellow show the valid way to write down an album:

~~~txt
Shortsighted Client,2018,songs:
{
    Each Panics,1.2 minutes,2005,175
    |Petri Stiller,0.5 minutes,2012,135
}
~~~

~~~txt
  Shortsighted Client,2018,songs:{
            Each Panics,1.2 minutes,2005,175
    |Petri Stiller,0.5 minutes,2012,135
}
~~~

~~~txt
  Shortsighted Client,2018,songs:{
            Each Panics,1.2 minutes,2005,175

    |
    Petri Stiller,0.5 minutes,2012,135

}
~~~

~~~txt
Shortsighted Client,2018,songs:
{
    Each Panics,1.2 minutes,2005,175|Petri Stiller,0.5 minutes,2012,135
}
~~~

~~~txt
Shortsighted Client,2018,songs:{Each Panics,1.2 minutes,2005,175|Petri Stiller,0.5 minutes,2012,135}
~~~

You are guaranteed that except prefix of whitespaces and endlines at the end of the line, there are no other symbols in the data. That means, if you strip whitespaces around the line and combine all the lines togather without endlines, you get a single string that contains only the data and seperating symbols as described in above texts.

# IMPORTANT

* Using the template is mandatory!
* All classes should be written in appropriate files. Empty class declarations with names is already given.
* All functions, attributes should have exact same names as specified in this file.
* You are **NOT** allowed to use any extra imports except `itertools` and `functool`.
* You can create helper methods, functions and attributes inside of your classess. 
* Running either `python3 SpotiPy.py` or `python SpotiPy.py` command should compile and run your solution without problems!
* When you are done, zip only the 4 python files and name it `solution.zip` and upload it on teams. (Teams renaming your work is not a problem).

## Grading

Homework is worth 10 points in total.

* `Song` - 2 points
 * 0.5 for getters, attributes and constructor
 * 0.5 for setting duration, likes and unlikes
 * 1 for string conversion
* `Album` - 3 points
 * 0.5 for attributes, getters and constructor
 * 0.5 for adding songs
 * 0.5 for `sortBy`
 * 1 for specific sort methods
 * 0.5 for string conversion
* `Artist` - 2 points
 * 0.5 for attributes, getters and constructor
 * 1 for `mostLikedSong`, `leastLikedSong` and `totalLikes`
 * 0.5 for string conversion
* `SpotiPy` - 3 points
 * 0.5 for attributes, getters and constructor
 * 0.5 for adding artists
 * 1 for getting top trending songs/albums/artists.
 * 1 for `loadFromFile`
* __Proper variable/method/class naming and code style will be considered as well!__
