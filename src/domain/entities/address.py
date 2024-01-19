class Constraint:
    def __init__(
        self,
        id:int,
        user_id: int,
    ) -> None:
        self.id = id
        self.user_id = user_id 
class Address:
    def __init__(
        self,
        id: int,
        user_id: int,
        postal_code: str,
        uf: str,
        city: str,
        neighborhood: str,
        street: str,
        number: str,
        complement: str,
    ) -> None:
        super().__init__(id,user_id)
        self.postal_code = postal_code
        self.uf = uf
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.number = number
        self.complement = complement
