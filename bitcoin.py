import sys
import requests
import json



try:
    amount = sys.argv
    amount = float(amount[1])
    a = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    b = a.text


    b = json.loads(b)

    cost = 56115.1530/2 #(((b.get('bpi')).get('USD')).get('rate_float'))


    print(f"${amount*cost:,.4f}")
except IndexError:
    print("Пропущен аргумент командной строки")
except ValueError:
    print("Аргумент командной строки не число")
except requests.exceptions.ConnectionError:
    print("Ой-ёй! Где неупорядок... Кажется инета нету")
