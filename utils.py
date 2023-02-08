import requests
from pprint import pprint

def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно"
        return None, f"ERROR: status_code:{response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"

