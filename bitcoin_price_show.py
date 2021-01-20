import requests


# you must connect to tor if your location restricted
# you can comment out proxy line and delete proxy arg for get method
def extract_bit_price():
    proxy = {"http" : "socks5://127.0.0.1:9050", "https" : "socks5://127.0.0.1:9050"}

    res = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json", proxies=proxy)


    bitcoin_price = (res.json()["bpi"]["USD"]["rate"])

    print("Bitcoin price is %s$" % bitcoin_price)

if __name__ == '__main__':
    extract_bit_price()
