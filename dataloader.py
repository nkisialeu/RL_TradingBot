from gym_trading_env.downloader import download
import datetime
import asyncio
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Download BTC/USDT historical data from Binance and stores it to directory ./data/binance-BTCUSDT-1h.pkl
download(exchange_names = ["binance"],
    symbols= ["BTC/USDT"],
    timeframe= "1h",
    dir = "data",
    since= datetime.datetime(year= 2020, month= 1, day=1),
    #until = datetime.datetime(year= 2021, month= 1, day=1)
)

df = pd.read_pickle("./data/binance-BTCUSDT-1h.pkl")
df.to_csv('pricedata.csv', index = False)