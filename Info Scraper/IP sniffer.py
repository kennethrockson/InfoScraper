import requests

def geolocate_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"DNS: {data['as']}")
    else:
        print("Failed to geolocate IP")

# Enter IP below
geolocate_ip("HERE")
