# Reinforcement Learning Trading Bot [RU]

![Снимок экрана 2024-12-07 221202](https://github.com/user-attachments/assets/0479520a-0e53-4d03-bce2-b950bfb93196)


## Описание

Этот проект представляет собой биткоин трейдинг бота, использующего алгоритмы обучения с подкреплением для торговли на рынке криптовалют. Бот обучается на исторических данных и способен принимать решения о покупке, продаже или удержании активов в зависимости от текущего состояния рынка. Основная задача бота — максимизация прибыли, используя стратегии, основанные на анализе исторических цен и других рыночных данных.

## Особенности

- **Модели**: Использует архитектуры нейронных сетей, такие как CNN и LSTM, для анализа временных рядов.
- **Обучение с подкреплением**: Реализует алгоритм Proximal Policy Optimization (PPO) для обучения торговых стратегий.
- **Гибкость**: Легко настраиваемые параметры, такие как размер окна, скорость обучения и количество эпох.
- **Визуализация**: Визуализация процесса торговли и результатов обучения, что позволяет отслеживать эффективность бота в реальном времени.
- **Поддержка GPU**: Оптимизирован для работы с графическими процессорами, что ускоряет процесс обучения.

## Библиотеки

- numpy
- tensorflow
- opencv-python
- matplotlib
- tensorboardx
- pandas
- mplfinance

Установите все необходимые библиотеки с помощью:

```bash
pip install -r requirements.txt
```
###

# Reinforcement Learning Trading Bot [EN]

## Description

This project is a bitcoin trading bot that uses reinforcement learning algorithms to trade in the cryptocurrency market. The bot is trained on historical data and can make decisions to buy, sell, or hold assets based on the current state of the market. The main goal of the bot is to maximize profits by employing strategies based on the analysis of historical prices and other market data.

## Features

- **Models**: Utilizes neural network architectures such as CNN and LSTM for time series analysis.
- **Reinforcement Learning**: Implements the Proximal Policy Optimization (PPO) algorithm for training trading strategies.
- **Flexibility**: Easily configurable parameters, such as window size, learning rate, and number of epochs.
- **Visualization**: Visualizes the trading process and training results, allowing for real-time monitoring of the bot's performance.
- **GPU Support**: Optimized for use with graphics processing units, accelerating the training process.

## Libraries

- numpy
- tensorflow
- opencv-python
- matplotlib
- tensorboardx
- pandas
- mplfinance

Install all necessary libraries using:

```bash
pip install -r requirements.txt
```
