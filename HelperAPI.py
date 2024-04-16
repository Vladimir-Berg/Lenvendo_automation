from ModelAPI import JsTestTask


def js_test_task(api_client):
    url = "https://www.lenvendo.ru/api/js-test-task/"
    products_list = []

    page = 1
    get_params = {'search': 'Alcatel', 'sort_field': 'name', 'page': str(page)}
    response = api_client.get(url, params=get_params)
    data = response.json()

    while data['next_page_url'] is not False:
        for item in data['products']:
            print(item)
            products_list.append(item)
        page += 1
        get_params['page'] = str(page)
        response = api_client.get(url, params=get_params)
        data = response.json()
    if data['next_page_url'] == False:
        for item in data['products']:
            products_list.append(item)

    print('@products_list@', products_list)
    objects = [JsTestTask(**item) for item in products_list]
    return objects


def check_string_in_names(list_of_names):
    a = True
    for item in list_of_names:
        if "Alcatel" in item.name:
            print("\n" + 'GOOD')
        if "Alcatel" not in item.name:
            a = False
            break
    return a
