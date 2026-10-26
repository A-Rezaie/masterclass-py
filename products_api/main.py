from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id : int
    name : str
    price : float

products = []

@app.get("/")
def home():
    return {"message": "Hello"}

@app.post("/products")
def create_product(product: Product):
    for existing_product in products:
        if existing_product.id == product.id:
            raise HTTPException(status_code=409 , detail="Product ID already exists")
        
    products.append(product)
    return product

@app.get("/products")
def get_products(max_price: float | None = None):
    if max_price is None:
        return products

    filtered_products = []
    for product in products:
        if product.price < max_price:
            filtered_products.append(product)
    return filtered_products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404 , detail="Product not found")
    
@app.put("/products/{product_id}")
def update_product(product_id : int, updated_product: Product):
    if updated_product.id != product_id:
        raise HTTPException(
            status_code=400,
            detail="Body ID must match path ID"
        )
    for product in products:
        if product.id == product_id:
            product.name = updated_product.name
            product.price = updated_product.price
            return product
    raise HTTPException(status_code=404 , detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted"}

    raise HTTPException(status_code=404 , detail="Product not found")
    