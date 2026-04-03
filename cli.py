import argparse
import logging

from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

# You can put real keys or dummy (fallback will handle)
API_KEY = "test"
API_SECRET = "test"

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float, help="Required for LIMIT")

args = parser.parse_args()

try:
    # ✅ Validation
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    client = BinanceClient(API_KEY, API_SECRET)

    # 📤 Request
    print("\n📤 ORDER REQUEST")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.type == "LIMIT":
        print(f"Price: {args.price}")

    # 🚀 Place Order
    response = create_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    # 📥 Response
    print("\n📥 ORDER RESPONSE")

    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Avg Price: {response.get('avgPrice')}")

    if "note" in response:
        print(f"Note: {response.get('note')}")

    logging.info(f"SUCCESS: {response}")

except Exception as e:
    print("\n❌ ERROR:", str(e))
    logging.error(f"ERROR: {str(e)}")