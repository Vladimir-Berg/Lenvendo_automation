from CardsPage import CardDenominations
import time


def test_click_value_of_cards(browser):
    main_page = CardDenominations(browser)
    main_page.open_base_page()
    time.sleep(2)
    main_page.click_on_card_denominations()