import time
from selenium.webdriver.common.by import By
from BaseApp import BaseApp


class CardDenominations(BaseApp):

    def click_on_card_denominations(self):
        wd = self.driver

        element = wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(1) > .par-options__button")
        position = element.location
        for i in range(0, position['y'], 50):
            wd.execute_script(f"window.scrollTo(0, {i})")
            time.sleep(0.04)  # для наглядности
        time.sleep(2)

        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(1) > .par-options__button").click()
        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(2) nobr").click()
        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(3) nobr").click()
        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(4) > .par-options__button").click()
        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(5)").click()
        wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(6) > .par-options__button").click()
