import requests

api_url = "https://api.openweathermap.org/data/2.5/weather?q=Rawalpindi&appid=2db1692bb14146238fc858b10697e794"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erorr {response.status_code}")