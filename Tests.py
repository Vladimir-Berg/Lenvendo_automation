import HelperAPI
from CardsPage import CardDenominations
import time


def test_click_value_of_cards(browser):
    main_page = CardDenominations(browser)
    main_page.open_base_page()
    time.sleep(2)
    list_of_denominations = main_page.go_to_card_denominations()
    for x in range(0, len(list_of_denominations)):
        active, text = main_page.check_value_and_active(list_of_denominations, x)
        assert active == True
        assert text == main_page.get_value_from_field()


def test_get_todo(api_client):
    list_of_names = HelperAPI.get_phones(api_client)
    a = HelperAPI.check_string_in_names(list_of_names)
    assert a == True
    assert sorted(list_of_names) == list_of_names
