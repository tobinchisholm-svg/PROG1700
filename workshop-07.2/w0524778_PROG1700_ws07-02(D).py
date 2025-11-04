songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]
least_played_song = ""
least_played_play = 0
most_played_song = ""
most_played = 0
#loop to print all songs with play counts
for i in range(len(songs)):
    print(f"{songs[i]}: {plays[i]}")
    if plays[i] > most_played:
        most_played = plays[i]
        most_played_song = plays[i]
    