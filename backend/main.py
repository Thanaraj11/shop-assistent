from fastapi import FastAPI
from backend.routes.chat import router as chat_router
from backend.routes.products import router as products_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(products_router)