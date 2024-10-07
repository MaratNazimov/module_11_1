from datetime import datetime, date
import requests
import matplotlib.pyplot as plt


URL = 'https://blockchain.info/ru/ticker'
x_axis = []
y_axis = []

def scrape():
    response = requests.get(URL)
    response_json = response.json()
    return float(response_json["USD"]["last"])

def axis_():
    latest_price = scrape()
    if latest_price == y_axis:
        pass
    elif latest_price != y_axis:
        tame_now = datetime.now()
        x_axis.append(str(f'{tame_now.hour}:{tame_now.minute}'))
        y_axis.append(latest_price)
        print(f'Значения с сайта:{y_axis}')

def pyplot_():
    plt.ion()
    while True:
        axis_()
        plt.xlabel(f'Дата: {date.today()}')
        plt.ylabel('USD')
        plt.title('Пара BTC|USD')
        plt.plot(x_axis, y_axis, color='green', marker='o', markersize=5, alpha=0.3)
        plt.grid(True)

        plt.pause(60)  # Информация на сайте обновляется раз в минуту

pyplot_()
