import data_download as dd
import data_plotting as dplt
'''Основная функция, управляющая процессом загрузки,
 обработки данных и их визуализации. 
 Запрашивает у пользователя ввод данных, 
 вызывает функции загрузки и обработки данных, 
 а затем передаёт результаты на визуализацию.'''


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите максимальный порог колебаний (например, 20): "))

    # Получение данных о запасах
    stock_data = dd.fetch_stock_data(ticker, period)

    # Добавьте скользящее среднее значение к данным
    stock_data = dd.add_moving_average(stock_data)

    # индикатор MACD
    ind_macd = dd.indicator_macd(stock_data)

    # Построим график данных
    dplt.create_and_save_plot(stock_data, ticker, period, ind_macd)

    # выводит среднюю цену закрытия акций за заданный период.
    print(dd.calculate_and_display_average_price(stock_data))

    # уведомляет если превышен порог
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # экспортировать данные в CSV формате
    dd.export_data_to_csv(stock_data, 'information_about_promotions.csv')




if __name__ == "__main__":
    main()
