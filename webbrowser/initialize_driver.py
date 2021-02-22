from selenium import webdriver


USERNAME = 'victo'  # имя пользователя в системе


def initialize_driver(path='chromedriver.exe'):
    # указываем какой файл с сохраннеными данными (паролями, например) использовать
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        f"user-data-dir=C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

    # получаем готовый для работы вебраузер
    driver = webdriver.Chrome(
        executable_path=path,           # путь к chromedriver.exe
        chrome_options=chrome_options)
    driver.implicitly_wait(2)  # ждем немножко, чтобы браузер успел открыться
    return driver

