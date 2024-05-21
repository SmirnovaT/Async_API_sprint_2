import aiohttp

url = "http://service:8000/api/v1/films/"
client_session = aiohttp.ClientSession()
while True:
    raw_response = await client_session.get(url)
    status = raw_response.status
    if status == 200:
        break