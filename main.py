from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="ERP Python Analytics Service", version="1.0")

class StockItem(BaseModel):
    name: str
    quantity: float
    purchase_price: float

class InvoiceItem(BaseModel):
    name: str
    quantity: float
    price: float

@app.get("/")
def root():
    return {"service": "ERP Python Analytics", "status": "running"}

@app.post("/analytics/stock-valuation")
def stock_valuation(items: List[StockItem]):
    value = sum(i.quantity * i.purchase_price for i in items)
    return {"inventory_value": round(value, 2), "item_count": len(items)}

@app.post("/analytics/invoice-total")
def invoice_total(items: List[InvoiceItem], tax_percent: float = 18):
    subtotal = sum(i.quantity * i.price for i in items)
    tax = subtotal * tax_percent / 100
    return {
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "total": round(subtotal + tax, 2)
    }
