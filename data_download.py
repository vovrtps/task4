import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    '''Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными.'''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def calculate_and_display_average_price(data):
    '''Ищет среднюю цену закрытия акций за заданный период'''
    df = data['Close'].tolist()
    ddf = sum(df)
    return ddf / len(df)


def notify_if_strong_fluctuations(data, threshold):
    '''Уведомляет если превышен порог'''
    df = pd.DataFrame(data['Close'])
    df_max = df.max()
    df_min = df.min()
    difference = (float(df_max.iloc[0] - float(df_min.iloc[0])))
    if difference > threshold:
        print('Превышен заданный порог')


def export_data_to_csv(data, filename):
    '''экспортировать данные в CSV формате'''
    df = pd.DataFrame(data)
    df.to_csv(filename, encoding='utf-8', index=False)


def add_moving_average(data, window_size=5):
    '''Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.'''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
