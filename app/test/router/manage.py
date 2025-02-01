from fastapi.testclient import TestClient
from app.main import app
from app.model.product import Product
from app.model.order import Order
from app.database import db_instance, db_session_wrapper
from app.schema.product import CreateProduct
from app.schema.order import CreateOrder
from app.type.order_status import OrderStatus



client = TestClient(app)



def test_add_product():
    response = client.post("/comm/products", json={
        "name": "Test Product",
        "description": "A test product",
        "price": 9.99,
        "stock": 100
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Product",
        "description": "A test product",
        "price": 9.99,
        "stock": 100
    }

def test_fetch_available_products():
    response = client.get("/comm/products")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "Test Product",
        "description": "A test product",
        "price": 9.99,
        "stock": 100
    }]

def test_create_order():
    response = client.post("/comm/products", json={
        "name": "Test Product 2",
        "description": "A test product",
        "price": 1,
        "stock": 100
    })
    # Attempting to test valid order with all products in stock
    response = client.post("/comm/orders", json={
        "products": [{"id": 1, "quantity": 51}, {"id":2, "quantity":51}]
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "products": [{"id": 1, "quantity": 51}, {"id":2, "quantity":51}],
        "total_price": 560.49,
        "status": "PENDING"
    }
    # Attempting to test invalid order with some products out of stock
    response = client.post("/comm/orders", json={
        "products": [{"id": 1, "quantity": 51}, {"id":2, "quantity":51}]
    })
    assert response.status_code == 409
    print(response.content)

if __name__=='__main__':
    # db_instance.delete_all_tables_and_metadata()
    test_add_product()
    test_fetch_available_products()
    test_create_order()