from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.product_repository import ProductRepositoryInterface
from src.domain.entities.product import Product
from src.infrastructure.database.models.product import Product as ProductModel


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_products(self) -> list[Product] | None:
        try:
            products = self.session.query(ProductModel).all()
            product_objects = []

            if products:
                for product_model in products:
                    product_data = {
                        "id": product_model.id,
                        "name": product_model.name,
                        "price": product_model.price,
                        "quantity": product_model.quantity,
                        "created_by_id": product_model.created_by_id,
                        "company_id": product_model.company_id,
                        "category": product_model.category.value,
                        "description": product_model.description,
                        "is_approved": product_model.is_approved,
                    }
                    product_object = Product(**product_data)
                    product_objects.append(product_object)

                return product_objects
            return products
        except:
            return None

    def get_product(self, id: int) -> Product | None:
        try:
            product_model = (
                self.session.query(ProductModel)
                .filter(ProductModel.id == id)
                .one_or_none()
            )

            if product_model:
                product_data = {
                    "id": product_model.id,
                    "name": product_model.name,
                    "price": product_model.price,
                    "quantity": product_model.quantity,
                    "created_by_id": product_model.created_by_id,
                    "company_id": product_model.company_id,
                    "category": product_model.category.value,
                    "description": product_model.description,
                    "is_approved": product_model.is_approved,
                }
                product_object = Product(**product_data)
                return product_object
            return product_model
        except:
            return None

    def create_product(
        self, product: Product, created_by_id: int, company_id: int
    ) -> Product | None:
        try:
            product_data = {
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity,
                "created_by_id": created_by_id,
                "company_id": company_id,
                "category": product.category,
                "description": product.description,
            }

            product_model = ProductModel(**product_data)

            self.session.add(product_model)
            self.session.commit()

            if product_model:
                product_data = {
                    "id": product_model.id,
                    "name": product_model.name,
                    "price": product_model.price,
                    "quantity": product_model.quantity,
                    "created_by_id": product_model.created_by_id,
                    "company_id": product_model.company_id,
                    "category": product_model.category.value,
                    "description": product_model.description,
                    "is_approved": product_model.is_approved,
                }
                product_object = Product(**product_data)
                return product_object

            return product_model
        except:
            return None

    def update_product(self, id: int, update_fields: dict[str, Any]) -> Product | None:
        try:
            self.session.query(ProductModel).filter(ProductModel.id == id).update(
                update_fields
            )
            self.session.commit()
            product_updated = self.get_product(id)

            return product_updated
        except:
            return None

    def delete_product(self, id: int) -> bool:
        try:
            self.session.query(ProductModel).filter(ProductModel.id == id).delete()
            self.session.commit()
            return True
        except:
            return False
