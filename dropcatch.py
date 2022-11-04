for n in range(100000000000000000000): #The number between the parentheses indicates how many times you will try the catch the domain.

    import requests

    url = "https://api.dynadot.com/api3.xml?key=[API-KEY]&command=register&duration=1&domain=[DOMAIN-HERE]"

#You need to replace your API key with [API-KEY] and also replace [DOMAIN-HERE] with the domain you want to catch.

#For example: url = "https://api.dynadot.com/api3.xml?key=7a6nf76sdf6gnd68fadnfs87dfgsd78fg7sdms&command=register&duration=1&domain=google.com"

    resp = requests.get(url)

    print(resp.status_code)
    print(resp.text)
    print(resp.elapsed.total_seconds())