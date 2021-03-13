
def parse_songs_list_content(content) -> list:
    # название_песни (берем)
    # автор (берем)
    # длительность (ее убираем)
    songs = []
    lines = content.split('\n')
    current_song = ''
    for line in lines:
        if ':' in line:
            songs.append(current_song[1:])
            current_song = ''
        else:
            current_song = current_song + ' ' + line
    return songs
