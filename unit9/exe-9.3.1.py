def my_mp3_playlist(file_path):
    longest_song = ''
    longest_song_length = 0
    num_songs = 0
    performers = {}

    with open(file_path) as f:
        for line in f:
            song_info = line.strip().split(';')
            song_name = song_info[0]
            performer = song_info[1]
            song_length = song_info[2]

            if int(song_length.split(':')[0]) > longest_song_length:
                longest_song = song_name
                longest_song_length = int(song_length.split(':')[0])

            if performer in performers:
                performers[performer] += 1
            else:
                performers[performer] = 1

            num_songs += 1

    most_common_performer = max(performers, key=performers.get)
    return longest_song, num_songs, most_common_performer


if __name__ == '__main__':
    print(my_mp3_playlist("D:/Desktop/python/songs.txt"))
