from sqlalchemy.orm import Session

from src.data.repositories.product_image_repository import (
    ProductImageRepositoryInterface,
)
from src.domain.entities.product import Product
from src.domain.entities.product_image import ProductImage
from src.infrastructure.database.models.product_image import (
    ProductImage as ProductImageModel,
)


class ProductImageRepository(ProductImageRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_product_images(self, product: Product) -> list[ProductImage] | None:
        try:
            return (
                self.session.query(ProductImageModel)
                .filter_by(product_id=product.id)
                .all()
            )
        except:
            return None

    def get_product_image(self, id: int) -> ProductImage | None:
        try:
            return (
                self.session.query(ProductImageModel)
                .filter(ProductImageModel.id == id)
                .one_or_none()
            )
        except:
            return None

    def create_product_image(self, product_image: ProductImage) -> ProductImage | None:
        try:
            product_image_data = {
                "product_id": product_image.product_id,
                "image": product_image.image,
            }
            product_image_model = ProductImageModel(**product_image_data)

            self.session.add(product_image_model)
            self.session.commit()
            self.session.refresh(product_image_model)
            return product_image_model
        except:
            return None

    def delete_product_image(self, id: int, product_id: int) -> bool:
        try:
            self.session.query(ProductImageModel).filter(
                ProductImageModel.id == id, ProductImageModel.product_id == product_id
            ).delete()
            self.session.commit()
            return True
        except:
            return False
