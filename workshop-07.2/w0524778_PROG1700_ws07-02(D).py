songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]
least_played_song = ""
least_played = 100
most_played_song = ""
most_played = 0
#loop to print all songs with play counts
for i in range(len(songs)):
    print(f"{songs[i]}: {plays[i]}")
    if plays[i] > most_played:
        most_played = plays[i]
        most_played_song = songs[i]
    if plays[i] > least_played:
        least_played = plays[i]
        least_played_song = songs[i]
print(f"The most played song is {most_played_song} with {most_played} plays")
print(f"the least played song is {least_played_song} wiht {least_played} plays")
    