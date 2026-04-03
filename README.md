# Binance Futures Trading Bot (Testnet)

A CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet with proper structure, validation, logging, and error handling.

---

## Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* Command Line Interface (CLI) using `argparse`
* Input validation for safe execution
* Structured modular code (client, orders, validators, logging)
* Logging of API requests, responses, and errors
* Fallback mechanism: simulated order execution if API is unavailable

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
```

---

## Setup Instructions

### Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Configure API Keys (Optional)

You can add your Binance API keys in `cli.py`:

```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
```

> Note: The bot uses Binance Futures Testnet. If API access is unavailable, it automatically switches to simulation mode.

---

## How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Sample Output

```
 ORDER REQUEST
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

 API failed, switching to simulated order...

 ORDER RESPONSE
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: market_price
Note: Simulated order (API unavailable)
```

---

##  Logging

All API requests, responses, and errors are logged in:

```
bot.log
```

---

## Error Handling

The application handles:

* Invalid input values
* Missing parameters
* API/network failures

---

## Fallback Mechanism

If Binance API is unavailable or restricted, the bot automatically switches to a simulated order system to ensure uninterrupted functionality.

---

## Assumptions

* User provides a valid trading symbol (e.g., BTCUSDT)
* Quantity is a positive number
* Price is required only for LIMIT orders

---

## Highlights

* Clean and modular architecture
* Production-like error handling
* Real-world fallback design
* Easy to extend for additional order types

---

## Future Improvements

* Add Stop-Limit / OCO orders
* Interactive CLI (menu-based UI)
* Web-based dashboard
* Real-time price tracking

---

## Author

**Anjali Aggarwal**
BTech CSE (AI) | MERN Stack Developer
