# Name: Matteo Borgio
# Partner: /
# Date: 19/11/2024
# Class: 3 A/INFO

# ***INSTRUCTIONS***
# Create your own copy of this code. Then follow the instructions to complete numbers 1 through 5.
# Write all of your code between the sets of asterisks for each problem.


print('\n#1: FAVORITE MUSICAL GENRES\n')
# 1. Fill in the code below to ask the user for 4 different genres of music. Add each genre to a list called music_genres.

# This code uses a loop (for i in range) where i is an integer each time the loop runs.

# **************************************** 
music_genres = []

for i in range(4):
  genere = input(f"Inserisci un genere musicale: ")
  music_genres.append(genere)

print(music_genres)

# **************************************** 


print('\n#2: FAVORITE ARTISTS\n')
# 2. Fill in the code below to ask the user for their favorite singer or band in each genre. Add their responses to a list called favorite_artists

# Note about the loop:
#
# This code uses a loop (for each) where genre is an element in the list music_genres each time the loop runs.
# Example: if music_genres = ['pop', 'rock', 'soul'], then genre will be 'pop', then 'rock', then 'soul'

# **************************************** 
favorite_artists = []

for genre in music_genres:
  artista = input(f"Inserisci un artista o una band per il genere {genre}: ")
  favorite_artists.append(artista)

print(favorite_artists)
  

# **************************************** 


print('\n#3: PRINT ARTISTS AND GENRES\n')
# 3. In the following loop, print out the user's favorite artists and their corresponding genres.

# **************************************** 


for i in range(len(favorite_artists)):
  print(f"Artista o band: {favorite_artists[i]}, Genere: {music_genres[i]}")


# **************************************** 


print('\n#4: HOW MANY PERMUTATIONS\n')
# 4. How many different permutations are there of artists and genres?

# Answer:
print("Le possibili permutazioni sono: ", len(music_genres) * len(favorite_artists))


print('\n#5: NESTED LOOP - GET PERMUTATIONS\n')
# 5. Write a nested loop to get all of the different permutations of genres and artists. User a counter to keep track of which permutation you're on and print it to the console each time the inner loop runs.

# **************************************** 

contatore = 0

for genere in music_genres:
  for artista in favorite_artists:
    print(f"Permutazione {contatore+1}: Genere: {genere}, Artista: {artista}")
    contatore += 1


# ****************************************