import requests

#

# xQrEgrxzRNcbOlHeMERWaoY5uAp27T
import requests


pages = 1

for p in range(pages):
    print(10 * p)
    response = requests.get(
        url="https://api.predicthq.com/v1/events/",
        headers={
            "Authorization": "Bearer xQrEgrxzRNcbOlHeMERWaoY5uAp27T",
            "Accept": "application/json"
        },
        params={
            "country": "US",
            "offset": "20",
            "active.gte": "2017-10-29T00:00:00Z",
            "active.lte": "2018-11-01T00:00:00Z"
        }
    )
    print(response.json())