songs = ["Song A", "Song B", "Song C", "Songs A", "Songs B"]
plays = [5, 10, 7, 5, 10]

least_played_song = ""
least_played = 10000
most_played_song = ""
most_played = 0
#total plas amd average per song
avg_play_per_song = 0
total_plays = 0

#bonus: allow user to add new songs interactively

try:
    new_song = input("Enter a new song for the playlist: ")
    # using methods
    songs.append(new_song)
    plays.append(0)
    
except:
    print(f"That is a terrible song")


#loop to print all songs with play counts
for i in range(len(songs)):
    print(f"{songs[i]}: {plays[i]}")
    if plays[i] > most_played:
        most_played = plays[i]
        most_played_song = songs[i]
    if plays[i] < least_played:
        least_played = plays[i]
        least_played_song = songs[i]
unique_songs = set(songs)
unique_plays = set(plays)
print(f"The most played song is {most_played_song} with {most_played} plays")
print(f"the least played song is {least_played_song} with {least_played} plays")
print(f"{unique_songs}, {unique_plays}")
# calculate total plays and average per song.
# convert the deplicated set to a list. 

unique_plays_list = list(unique_plays)
for i in range(len(unique_plays)):
   # total_plays += unique_plays[i]
    avg_play_per_song = total_plays / len(unique_plays_list)
print(f"Toal plays:{total_plays}. The avg play per son is {avg_play_per_song:.0}")
