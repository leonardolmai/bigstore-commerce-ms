from datetime import datetime


class Order:
    def __init__(
        self,
        id: int,
        user_id: int,
        company_id: int,
        status: str,
        created_at: datetime,
        payment_method: str,
        payment_details: str,
        delivery_address: str,
        total: float,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.company_id = company_id
        self.status = status
        self.created_at = created_at
        self.payment_method = payment_method
        self.payment_details = payment_details
        self.delivery_address = delivery_address
        self.total = total
