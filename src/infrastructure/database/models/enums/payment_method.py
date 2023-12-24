from enum import Enum


class PaymentMethod(Enum):
    CARD = "card"
    PIX = "pix"
    BANK_SLIP = "bank_slip"
