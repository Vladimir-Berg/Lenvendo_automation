import HelperAPI
from CardsPage import CardDenominations
import time
import allure


@allure.title("Check active and selected card value in input-field")
def test_click_value_of_cards(browser):
    main_page = CardDenominations(browser)
    with allure.step("Open base page"):
        main_page.open_base_page()
    time.sleep(2)
    list_of_denominations = main_page.go_to_card_denominations()
    with allure.step(f"Checking"):
        for x in range(0, len(list_of_denominations)):
            active, text = main_page.check_value_and_active(list_of_denominations, x)
            with allure.step(f"Check active: {text}"):
                assert active == True
            with allure.step(f"Check selected card value in input-field: {main_page.get_value_from_field()}"):
                assert text == main_page.get_value_from_field()


@allure.title("Test API")
def test_check_sorting_and_alcatel(api_client):
    list_of_names = HelperAPI.js_test_task(api_client)
    a = HelperAPI.check_string_in_names(list_of_names)
    with allure.step("All names include 'Alcatel'"):
        assert a == True
    with allure.step("Right sorting"):
        assert sorted(list_of_names) == list_of_names
