def calculate_item_value(price: float, stock: int) -> float:
    """Multiplica el precio por la cantidad en stock."""
    return price * stock

def get_out_of_stock(products: list[dict]) -> list[str]:
    """Devuelve los nombres de productos con stock cero."""
    # [que_guardo for elemento in coleccion if condicion]
    return [product["name"] for product in products if product["stock"] == 0]

def filter_by_min_price(products: list[dict], min_price: float = 50.0) -> list[str]:
    """Devuelve los nombres de productos cuyo precio es igual o supera el min."""
    return [
        product["name"] for product in products 
        if product["price"] >= min_price
        ]

def main() -> None:
    """Run the main program logic"""
products = [
    {"name": "Laptop", "price": 899.99, "stock": 5},
    {"name": "Mouse", "price": 19.50, "stock": 25},
    {"name": "Keyboard", "price": 45.00, "stock": 0},
    {"name": "Monitor", "price": 199.99, "stock": 8},
    {"name": "Webcam", "price": 35.00, "stock": 0},
]

out_of_stock = get_out_of_stock(products)
expensive_items = filter_by_min_price(products)

print("Out of stock: ", out_of_stock)
print("Expensive items: ", expensive_items)

if __name__ == "__main__":
    main()

