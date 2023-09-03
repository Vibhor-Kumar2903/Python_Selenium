import json

import requests

base_url = "https://petstore.swagger.io/v2"


def get_request_1(base_url, petID):
    url = base_url + f"/pet/{petID}"
    # headers = {content-type : "application/json"}

    response = requests.get(url=url)
    json_response = response.json()
    beautify_json = json.dumps(json_response, indent=4)
    assert response.status_code == 200

    print(beautify_json)


petID = "3"
get_request_1(base_url, petID)
