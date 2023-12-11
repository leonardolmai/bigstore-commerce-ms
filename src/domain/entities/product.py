class Product:
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        quantity: int,
        created_by_id: int,
        company_id: int,
        category: str,
        description: str | None = None,
        is_approved: bool = False,
    ) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.created_by_id = created_by_id
        self.company_id = company_id
        self.category = category
        self.description = description
        self.is_approved = is_approved
