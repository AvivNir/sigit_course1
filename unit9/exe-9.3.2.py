def my_mp4_playlist(file_path, new_song):
    songs = open(file_path, 'r')
    songs_lst = " "
    for line in songs:
        songs_lst += line

    songs_lst = songs_lst.replace('\n', "")
    my_list = songs_lst.split(';')
    my_list[6] = new_song
    songs = open(file_path, 'w+')
    for i in range(0, len(my_list) - 3, 3):
        songs.write(my_list[i] + ";" + my_list[i + 1] + ";" + my_list[i + 2] + ";" + "\n")


if __name__ == '__main__':
    my_mp4_playlist("D:/Desktop/python/songs.txt", "Python Love Story")
