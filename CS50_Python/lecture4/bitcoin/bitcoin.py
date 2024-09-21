import requests
import sys

while True:
    if len(sys.argv) == 2:
        try:
            f = float (sys.argv[1])
            z = True
            break
        except ValueError:
            print ("Command-line argument is not a number")
            z = False
            sys.exit(1)
    else:
        print ("Mising command-line argument")
        z = False
        sys.exit(1)

if z == True:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    a = response.json()
    b = a.get("bpi")
    c = b.get("USD")
    d = c.get("rate_float")
    f = float (sys.argv[1])
    e = d * f
    print (f"${e:,.4f}")
