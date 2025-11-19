# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name: str, album_title: str, song_number: int = None):

    album: dict = {
        "Artist Name": artist_name,
        "Album Name": album_title,
    }

    if song_number != None:
        album["Number of Songs"] = song_number

    print(album)

make_album("Radiohead", "OK Computer")

print("")

make_album("Beyoncé", "RENAISSANCE")

print("")

make_album("Kendrick Lamar", "DAMN", 12)

# 8-8. User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

print("")

while True:
    artist = input("Inserisci il nome di un artista: ")
    album = input("Inserisci il nome dell'album: ")

    make_album(artist, album)

    continua = input("Vuoi inserire un'altro album? (No per uscire): ")

    if continua.lower() == "no":
        break