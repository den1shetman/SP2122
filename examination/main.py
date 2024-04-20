import logging
from htmlparser import HtmlParser

logging.basicConfig(filename='user_actions.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    print("Виберіть:")
    print("1 - Обмін валют")
    print("2 - Подивитись погоду")

    choice = input("Введіть номер опції: ")

    try:
        choice = int(choice)
    except ValueError:
        logging.error(f"Некоректний ввід: {choice}")
        print("Будь ласка, введіть число.")
        return

    if choice == 1:
        parser = HtmlParser("https://bank.gov.ua/")
        parser.HtmlParse('div', 'index-page')
        print(parser.Result)
        digit = float(input("Enter digit (гривні): "))
        print(digit / parser.Result[3] )

    elif choice == 2:
        weather_parser = HtmlParser("https://meteo.ua/ua/34/kiev")
        weather_parser.HtmlParse('div', 'weather-detail__main-temp')
        print(f'Зараз температура повітря у Києві +{weather_parser.Result[0]} градусів')
    else:
        logging.error(f"Некоректний вибір опції: {choice}")
        print("Некоректний вибір опції. Будь ласка, введіть 1 або 2.")

if __name__ == "__main__":
    main()