import requests
import fire

def get(url):
    try:
        r = requests.get(url)
        return r.text
    except Exception as ex:
        return ex

if __name__ == '__main__':
    fire.Fire({
        'GET': get
    })