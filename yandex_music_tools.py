from webbrowser.tools import universal_click


FIRST_SONG_LIKE_BUTTON_XPATH = '/html/body/div[1]/div[9]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/span[1]/span/span[2]'
def like_song(driver, song_name):
    # открываем яндекс музыку и ищем нужную композицию
    driver.get(f'https://music.yandex.ru/search?text={song_name}')
    driver.implicitly_wait(2)
    # получаем нужную кнопку
    like_button = driver.find_element_by_xpath(FIRST_SONG_LIKE_BUTTON_XPATH)
    driver.implicitly_wait(2)
    if 'сделайте' not in like_button.get_attribute('title'):
        # эта песня уже у нас в библиотеке
        universal_click(driver, like_button)  # кликнем, чтобы удалить из нашего плейлиста
        # кнопка изменилась, получаем ее еще раз
        like_button = driver.find_element_by_xpath(FIRST_SONG_LIKE_BUTTON_XPATH)
        driver.implicitly_wait(2)
    universal_click(driver, like_button)  # добавим

