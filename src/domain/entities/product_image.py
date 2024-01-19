class ProductImage:
    def __init__(
        self,
        id: int,
        product_id: int,
        image: str,
    ) -> None:
        self.id = id
        self.product_id = product_id
        self.image = image
