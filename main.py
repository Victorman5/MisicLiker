from webbrowser.initialize_driver import initialize_driver
import yandex_music_tools as yandex


if __name__ == '__main__':
    # получаем драйвер, открываем браузер
    driver = initialize_driver('webbrowser//chromedriver.exe')
    # лайкаем песенку
    try:
        yandex.like_song(driver, "wildways lost")
    except Exception as e:
        print(e)

    driver.close()

