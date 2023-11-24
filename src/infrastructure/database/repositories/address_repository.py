from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.address_repository import AddressRepositoryInterface
from src.domain.entities.address import Address
from src.infrastructure.database.models.address import Address as AddressModel


class AddressRepository(AddressRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_address(self, user_id) -> list[Address] | None:
        try:
            return (
                self.session.query(AddressModel)
                .filter(AddressModel.user_id == user_id)
                .all()
            )
        except:
            return None

    def get_address(self, id: int) -> Address | None:
        try:
            return (
                self.session.query(AddressModel)
                .filter(AddressModel.id == id)
                .one_or_none()
            )
        except:
            return None

    def create_address(self, address: Address, user_id: int) -> Address | None:
        try:
            address_data = {
                "user_id": user_id,
                "postal_code": address.postal_code,
                "uf": address.uf,
                "city": address.city,
                "neighborhood": address.neighborhood,
                "street": address.street,
                "number": address.number,
                "complement": address.complement,
            }
            address_model = AddressModel(**address_data)

            self.session.add(address_model)
            self.session.commit()

            return address_model

        except:
            return None

    def update_address(self, id: int, update_fields: dict[str, Any]) -> Address | None:
        try:
            self.session.query(AddressModel).filter(AddressModel.id == id).update(
                update_fields
            )
            self.session.commit()
            address_updated = self.get_address(id)

            return address_updated
        except:
            return None

    def delete_address(self, id: int) -> bool:
        try:
            self.session.query(AddressModel).filter(AddressModel.id == id).delete()
            self.session.commit()
            return True
        except:
            return False
