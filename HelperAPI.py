from ModelAPI import JsTestTask


def get_phones(api_client):
    url = "https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name"
    response = api_client.get(url)
    data = response.json()
    data = data['products']
    objects = [JsTestTask(**item) for item in data]
    return objects
