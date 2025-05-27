from awswaf.aws import AwsWaf
from curl_cffi import requests

session = requests.Session(impersonate="chrome")

session.headers = headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}
response = session.get("https://www.binance.com/")
goku = AwsWaf.extract_goku_props(response.text)

token = AwsWaf(goku, )()
session.headers.update({
    "cookie": "aws-waf-token=" + token
})
# print(session.headers)
print(token[:100])
print(len(session.get("https://www.binance.com/").text) > 2494)
