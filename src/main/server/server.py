from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.presentation.middlewares.cnpj_middleware import check_company_cnpj_middleware
from src.presentation.routers import (
    address_routers,
    card_routers,
    company_routers,
    order_routers,
    product_routers,
    token_routers,
    user_routers,
)

app = FastAPI()


app.middleware("http")(check_company_cnpj_middleware)

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["http://localhost:3000", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["Authorization"],
    # allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    # allow_headers=[
    #     "Accept",
    #     "Content-Type",
    #     "Origin",
    #     "Authorization",
    #     "X-CSRF-Token",
    #     "X-Requested-With",
    #     "X-Company-CNPJ",
    #     "Cache-Control",
    #     "If-None-Match",
    #     "Access-Control-Allow-Origin",
    #     "Access-Control-Allow-Methods",
    #     "Access-Control-Allow-Headers",
    #     "Authorization",
    #     "X-Company-CNPJ",
    # ],
)

app.include_router(user_routers.router)
app.include_router(token_routers.router)
app.include_router(company_routers.router)
app.include_router(address_routers.router)
app.include_router(card_routers.router)
app.include_router(product_routers.router)
app.include_router(order_routers.router)
