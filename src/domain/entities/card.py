class Constraint:
    def __init__(
        self,
        id: int,
        user_id: int,
    ) -> None:
        self.id = id
        self.user_id = user_id


class Card(Constraint):
    def __init__(
        self,
        id: int,
        user_id: int,
        name: str,
        number: str,
        expiration_month: str,
        expiration_year: str,
        cvc: str,
    ) -> None:
        super().__init__(id, user_id)
        self.name = name
        self.number = number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.cvc = cvc
