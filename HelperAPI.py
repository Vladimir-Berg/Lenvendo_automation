import allure

from ModelAPI import JsTestTask


@allure.step("Get list of products")
def js_test_task(api_client):
    url = "https://www.lenvendo.ru/api/js-test-task/"
    products_list = []

    page = 1
    get_params = {'search': 'Alcatel', 'sort_field': 'name', 'page': str(page)}
    response = api_client.get(url, params=get_params)
    data = response.json()

    while data['next_page_url'] is not False:
        with allure.step(f"Get list from {page} page"):
            for item in data['products']:
                products_list.append(item)
            page += 1
            get_params['page'] = str(page)
            response = api_client.get(url, params=get_params)
            data = response.json()
    if data['next_page_url'] == False:
        with allure.step(f"Get list from {page} page"):
            for item in data['products']:
                products_list.append(item)

    objects = [JsTestTask(**item) for item in products_list]
    return objects


@allure.step("Check that each name include 'Alcatel'")
def check_string_in_names(list_of_names):
    a = True
    for item in list_of_names:
        if "Alcatel" in item.name:
            pass
        if "Alcatel" not in item.name:
            a = False
            break
    return a
