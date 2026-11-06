# Products API

A FastAPI project for creating, listing, updating, and deleting products. Each product has an `id`, a `name`, and a `price`. Products are stored in memory and reset when the server restarts.

## Run locally

From the `products_api` directory, run these commands on Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8001
```

Open the [interactive API docs](http://127.0.0.1:8001/docs) while the server is running.

## Try it

In a second terminal, create a product and then list products priced below 100:

```bash
curl -X POST 'http://127.0.0.1:8001/products' \
  -H 'Content-Type: application/json' \
  -d '{"id": 1, "name": "Mouse", "price": 80}'

curl 'http://127.0.0.1:8001/products?max_price=100'
```

`max_price=100` returns products priced strictly below 100. Omit `max_price` to list all products.

## Endpoints

| Method | Path | Action |
| --- | --- | --- |
| GET | `/products` | List products with an optional price filter |
| POST | `/products` | Create a product |
| GET | `/products/{product_id}` | Get one product |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |
