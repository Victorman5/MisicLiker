from selenium.webdriver.common.action_chains import ActionChains


def universal_click(driver, element):
    ActionChains(driver).move_to_element(element).click().perform()
    driver.implicitly_wait(2)
