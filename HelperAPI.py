from ModelAPI import JsTestTask


def get_phones(api_client):
    url = "https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name"
    response = api_client.get(url)
    data = response.json()
    data = data['products']
    objects = [JsTestTask(**item) for item in data]
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
