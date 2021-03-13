from webbrowser.tools import universal_click
from selenium.common.exceptions import NoSuchElementException
from webbrowser.tools import scroll_to
from yandex.tools import parse_songs_list_content
from time import sleep


FIRST_SONG_LIKE_BUTTON_XPATH_IF_EXCEPTION = '/html/body/div[1]/div[9]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/span[1]/span/span[2]'
FIRST_SONG_LIKE_BUTTON_XPATH = '/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/span[1]/span/span[2]'
def like_song(driver, song_name):
    def get_like_button():
        try:
            button = driver.find_element_by_xpath(FIRST_SONG_LIKE_BUTTON_XPATH)
            driver.implicitly_wait(2)
        except NoSuchElementException as e:
            button = driver.find_element_by_xpath(FIRST_SONG_LIKE_BUTTON_XPATH_IF_EXCEPTION)
            driver.implicitly_wait(2)
        return button

    # открываем яндекс музыку и ищем нужную композицию
    driver.get(f'https://music.yandex.ru/search?text={song_name}')
    driver.implicitly_wait(2)
    sleep(2)  # ждем, пока загрузится реклама
    # получаем нужную кнопку
    like_button = get_like_button()
    if 'нравится' in like_button.get_attribute('title'):
        # эта песня уже у нас в библиотеке
        universal_click(driver, like_button)  # кликнем, чтобы удалить из нашего плейлиста
        # кнопка изменилась, получаем ее еще раз
        like_button = get_like_button()
        driver.implicitly_wait(2)
    universal_click(driver, like_button)  # добавим


SONGS_LIST_XPATH = 'html/body/div[1]/div[9]/div[2]/div/div/div[4]/div/div/div'
FOOTER_XPATH = '/html/body/div[1]/div[9]/div[4]/div[2]/div[2]'
def load_songs_from_playlist(driver, playlist_url):
    driver.get(playlist_url)
    sleep(2)

    # найдем же футер, чтобы понять, где конец страницы (плейлиста)
    footer = driver.find_element_by_xpath(FOOTER_XPATH)
    driver.implicitly_wait(2)

    songs = set()
    footer_y = footer.location['y']  # скроллить будем до конца страницы
    step = 2000
    for y in range(0, footer_y + step, step):
        # скроллим потихоньку
        scroll_to(driver, x=0, y=y)

        # берем подгруженные песенки
        lst = driver.find_element_by_xpath(SONGS_LIST_XPATH)
        driver.implicitly_wait(2)

        # парсим данные, чтобы достать названия композиций
        songs.update(parse_songs_list_content(lst.text))

    return songs

