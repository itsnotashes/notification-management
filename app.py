import requests

from notificationBot import NotificationBot

theWhiskeyExchange = NotificationBot("https://www.thewhiskyexchange.com")


# Headers
headers = {
    'authority': 'kit-pro.fontawesome.com',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'font',
    'referer': 'https://kit-pro.fontawesome.com/releases/latest/css/pro-v4-font-face.min.css',
    'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.thewhiskyexchange.com',
    'if-none-match': '"1601915095"',
    'if-modified-since': 'Mon, 05 Oct 2020 16:24:55 GMT',
    'Referer': 'https://www.thewhiskyexchange.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'DNT': '1',
    'Origin': 'https://www.thewhiskyexchange.com',
    'x-requested-with': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Accept-Language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
    'journey': 'true',
    'lastpage': 'https://www.thewhiskyexchange.com/new-products/standard-whisky',
}

theWhiskeyExchange.addHeaders(headers=headers, data=data)

response = theWhiskeyExchange.makeRequest(
    "https://www.thewhiskyexchange.com/new-products/standard-whisky", post=True)

print(response, file=open("random.html", 'w'))
