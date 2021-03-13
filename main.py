from webbrowser.initialize_driver import initialize_driver
import yandex.yandex_music_tools as yandex


if __name__ == '__main__':
    # получаем драйвер, открываем браузер
    driver = initialize_driver('webbrowser//chromedriver.exe')

    songs = yandex.load_songs_from_playlist(driver,
                        'https://music.yandex.ru/users/yamusic-bestsongs/playlists/6251472')

    print(len(songs), songs)

    for song in songs:
        yandex.like_song(driver, song)

    # driver.close()

