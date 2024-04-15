import time
from selenium.webdriver.common.by import By
from BaseApp import BaseApp


class CardDenominations(BaseApp):

    def go_to_card_denominations(self):
        wd = self.driver

        element = wd.find_element(By.CSS_SELECTOR, ".js-par-option:nth-child(1) > .par-options__button")
        position = element.location
        for i in range(0, position['y'], 50):
            wd.execute_script(f"window.scrollTo(0, {i})")
            time.sleep(0.04)  # для наглядности
        time.sleep(2)

        # Получение списка номиналов
        list_of_denominations = wd.find_elements(By.CLASS_NAME, 'par-options__button')
        return list_of_denominations

    def get_value_from_field(self):
        wd = self.driver
        value_input = wd.find_element(By.XPATH, '//*[@id="range-value-input"]').get_attribute("value")
        return value_input
