import random

def create_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        params["price"] = price
        params["timeInForce"] = "GTC"

    try:
       
        return client.place_order(**params)

    except Exception as e:
        
        print("⚠️ API failed, switching to simulated order...")

        return {
            "orderId": random.randint(100000, 999999),
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else "market_price",
            "note": "Simulated order (API unavailable)"
        }
