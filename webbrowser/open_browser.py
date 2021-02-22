from initialize_driver import initialize_driver


if __name__ == '__main__':
    driver = initialize_driver(path='chromedriver.exe')
    input("Press Enter to close browser:")
    driver.close()

