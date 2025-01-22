# Name: Matteo Borgio
# Partner: 
# Date: 20/11/2024
# Class: 3A/INFO
# Lab: MUSICAL ARTISTS AND GENRES Part 2 (input, loops, lists, functions)


# ***INSTRUCTIONS***
# Fork this replit to create your own copy. Then follow the instructions to complete numbers 6 through 10.
# Write all of your code between the sets of asterisks for each problem.

print('\n#6: FUNCTIONS - GENRES')
# 6. Turn your code from #1 into a function called 'getGenres'. 
#
# Fill in the code below with the missing parts. 
#
# The parameter 'times' is the number of genres you will get from the user. 
# Replace your for loop's existing range with the parameter name. 
# Return the list of genres.
# Call the function, passing it 3 as an argument, and save the returned list in a variable called 'genres'.

# ************************************

def getGenres(times):
  print('\n')
  music_genres = []
  for i in range(times):  
    genres = input(f"Inserisci un genere musicale: ")
    music_genres.append(genres)
  return music_genres

# paste your code from part 1 here

#return your list of genres here

# saves what's returned into the variable 'genres'

# ************************************


print('\n#7: FUNCTIONS - ARTISTS')
# 7. Turn your code from #2 into a function called 'getArtists'. 
# Your function should have one parameter called 'music_genres'.
# Return the list of favorite_artists.
# Call the function, passing it genres, and save the returned list in a variable called 'artists'.

# ************************************

def getArtists(music_genres):
  favorite_artists = []
  for genere in music_genres:
    artists = input(f"Inserisci un artista o una band per il genere {genere}: ")
    favorite_artists.append(artists)
  return favorite_artists


# ************************************


print('\n#8: FUNCTIONS - PRINT FAVORITES')
# 8. Turn your code from #3 into a function called 'printFavorites'. Your function should have two parameters called 'music_genres' and 'favorite_artists'. 
# This function doesn't need to return anything.
# Call the function, passing it genres and artists.

# ************************************

def printFavorites(music_genres, favorite_artists):
  for i in range(len(favorite_artists)):  
    print(f"Artista o band: {favorite_artists[i]}, Genere: {music_genres[i]}")


# ************************************


print('\n#9: FUNCTIONS - PRINT PERMUTATIONS')
# 9. Turn your code from #5 into a function called 'printPermutations'. 
# Your function should have two parameters called 'music_genres' and 'favorite_artists'. 
# This function doesn't need to return anything.
# Call the function, passing it genres and artists.

# ************************************

def printPermutations(music_genres, favorite_artists):
    contatore = 0
    for genere in music_genres:
        for artista in favorite_artists:
            print(f"Permutazione {contatore+1}: Genere: {genere}, Artista: {artista}")
            contatore += 1

# ************************************


print('\n#10: FUNCTIONS - TALK ABOUT MUSIC')
# 10. Create a new function called 'talkAboutMusic' that calls each of the functions written above, in order. 
# Ask the user how many favorite genres of music they have and pass that value when you call getGenres().
# Whenever a function returns a value, save that value in a variable for later use.
# Call the function twice.

# ************************************

def talkAboutMusic():
    numero_generi = int(input("Quanti generi musicali hai preferito? "))
    genres = getGenres(numero_generi)  
    favorite_artists = getArtists(genres)
    printFavorites(genres, favorite_artists)
    printPermutations(genres, favorite_artists)
    return genres, favorite_artists  

print(talkAboutMusic())
  


# ************************************