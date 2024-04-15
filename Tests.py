from CardsPage import CardDenominations
import time
from ModelAPI import JsTestTask


def test_click_value_of_cards(browser):
    main_page = CardDenominations(browser)
    main_page.open_base_page()
    time.sleep(2)
    list_of_denominations = main_page.go_to_card_denominations()
    for x in range(0, len(list_of_denominations)):
        list_of_denominations[x].click()
        text = list_of_denominations[x].text
        active = False
        if 'par-options__button--active' in list_of_denominations[x].get_attribute('class'):
            active = True
        assert active == True
        assert text == main_page.get_value_from_field()


def test_get_todo(api_client):
    url = "https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name"
    response = api_client.get(url)
    data = response.json()
    data = data['products']
    objects = [JsTestTask(**item) for item in data]
    print(objects)
#    assert data["title"] == "delectus aut autem"
