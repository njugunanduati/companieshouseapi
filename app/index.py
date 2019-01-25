import json
import requests
from app.sensitivewords import sensitivewords
from datetime import datetime
x = datetime.now()


api_endpoint = 'https://api.companieshouse.gov.uk'
api_key = 's524FiN5DUfCtjGB4uglfpOsy7nBf86q9ak12KbY'

class Index:

    def check_comapny_name(word):
        payload = {
            'q': word.upper(),
            'items_per_page': 100,
            'start_index': 1,
            'ts': x.timestamp()
        }
        try:
            a_list = [item for item in sensitivewords if item in word]
            while len(a_list) > 0:
                return "The comapny name {} contains this '{}' sensitive word".format(word, a_list[0])
            online_results = Index.check_online(payload)
            data = json.loads(online_results['message'])
            for item in data['items']:
                check_available = {k:v for (k, v) in item.items() if v == word}
                if len(check_available) == 0:
                    return "Congratulations! Comapny name {} is available".format(word)
                else:
                    return "The Comapny name '{}' is similar to '{}'.".format(word, check_available)
        except Exception as e:
            return str(e)

    def check_online(payload):
        url = api_endpoint+'/search/companies/'
        try:
            result = requests.get(url, data=payload, auth=(api_key, ''))
            data = {"status": "Success", "message": result.text}
        except Exception as e:
            data = {"status": "Error!", "message": str(e)}
        return data
