from CardsPage import CardDenominations
import time


def test_click_value_of_cards(browser):
    main_page = CardDenominations(browser)
    main_page.open_base_page()
    time.sleep(2)
    list_of_denominations = main_page.go_to_card_denominations()
    for x in range(0, len(list_of_denominations)):
        list_of_denominations[x].click()
        text = list_of_denominations[x].text
        assert text == main_page.get_value_from_field()
