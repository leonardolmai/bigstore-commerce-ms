from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.card_repository import CardRepositoryInterface
from src.domain.entities.card import Card
from src.infrastructure.database.models.card import Card as CardModel


class CardRepository(CardRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_card(self, user_id) -> list[Card] | None:
        try:
            return (
                self.session.query(CardModel).filter(CardModel.user_id == user_id).all()
            )
        except:
            return None

    def get_card(self, id: int) -> Card | None:
        try:
            return (
                self.session.query(CardModel).filter(CardModel.id == id).one_or_none()
            )
        except:
            return None

    def create_card(self, card: Card, user_id: int) -> Card | None:
        try:
            card_data = {
                "user_id": user_id,
                "name": card.name,
                "number": card.number,
                "expiration_month": card.expiration_month,
                "expiration_year": card.expiration_year,
                "cvc": card.cvc,
            }
            card_model = CardModel(**card_data)

            self.session.add(card_model)
            self.session.commit()

            return card_model

        except:
            return None

    def update_card(self, update_fields: dict[str, Any], id: int) -> Card | None:
        try:
            self.session.query(CardModel).filter(CardModel.id == id).update(
                update_fields
            )
            self.session.commit()
            card_updated = self.get_card(id)

            return card_updated
        except:
            return None

    def delete_card(self, id: int) -> bool:
        try:
            self.session.query(CardModel).filter(CardModel.id == id).delete()
            self.session.commit()
            return True
        except:
            return False
