from src.ecommerce import Product, OrderError, process_order
from datetime import datetime
import pytest

def test_process_valid_orders():
    product = Product(
        name = "denim_shirt",
        price = 10,
        stock = 1000
    )
    order_item = process_order(
        product = product,
        quantity = 100,
        is_premium_user = False,
        order_time = datetime.now()
    )
    assert order_item["total"] == 1000
    assert order_item["product"] == "denim_shirt"

def test_process_premium_user_order():
    product = Product(
            name = "iphone17",
            price = 1000,
            stock = 10
        )
    order_item = process_order(
        product = product,
        quantity = 2,
        is_premium_user = True,
        order_time = datetime.now()
    )
    assert order_item["total"] == 1800
    assert order_item["discount"] == 200

def test_process_stock_check():
    product = Product(
            name = "iphone17",
            price = 1000,
            stock = 10
        )
    order_item = process_order(
        product = product,
        quantity = 2,
        is_premium_user = True,
        order_time = datetime.now()
    )
    assert order_item["product"] == "iphone17"
    assert product.stock == 8


def test_exceed_quantity():
    product = Product(
            name = "iphone17",
            price = 1000,
            stock = 10
        )
    with pytest.raises(OrderError, match="Not enough stock available"):
        process_order(
            product = product,
            quantity = 12,
            is_premium_user = True,
            order_time = datetime.now()
        )

def test_invalid_quantity():
    product = Product(
            name = "iphone17",
            price = 1000,
            stock = 10
        )
    with pytest.raises(OrderError, match = "Quantity must be greater than 0"):
        process_order(
            product = product,
            quantity = 0,
            is_premium_user = True,
            order_time = datetime.now()
        )

def test_failed_order_does_not_change_stock():
    product = Product("samsung", 1000, 10)

    with pytest.raises(OrderError):
        process_order(
            product=product,
            quantity=12,
            is_premium_user=True,
            order_time=datetime(2026, 10, 26, 14, 0)
        )

    assert product.stock == 10