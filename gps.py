import requests

def Gps(address):
    ad_list = {}
    if address in ad_list.keys():
        pass
    else:
        url_front = "https://maps.googleapis.com/maps/api/geocode/json?"
        url_address = "&address="
        url_key = "&key="

        auth_key = 'AIzaSyCqBfVV_DrnKdd3vxUinjHkdE-ziz54XnU'

    # url 완성
        url = url_front + url_address + address + url_key + auth_key

        result = requests.get(url)
        json_data = result.json()
        ad_list[address] = [json_data['results'][0]['geometry']['location']['lat'],json_data['results'][0]['geometry']['location']['lng']]
        return ad_list
