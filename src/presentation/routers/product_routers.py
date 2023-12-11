# pylint: disable=unused-argument
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.product.create_product_composer import (
    create_product_composer,
)
from src.presentation.composers.product.delete_product_composer import (
    delete_product_composer,
)
from src.presentation.composers.product.get_product_composer import get_product_composer
from src.presentation.composers.product.list_products_composer import (
    list_products_composer,
)
from src.presentation.composers.product.update_product_composer import (
    update_product_composer,
)
from src.presentation.composers.product_image.create_product_image_composer import (
    create_product_image_composer,
)
from src.presentation.composers.product_image.delete_product_image_composer import (
    delete_product_image_composer,
)
from src.presentation.composers.product_image.list_product_images_composer import (
    list_product_images_composer,
)
from src.presentation.dependencies.get_current_company import get_current_company
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.company import CompanyOut
from src.presentation.schemas.product import ProductCreate, ProductOut, ProductUpdate
from src.presentation.schemas.product_image import ProductImageOut
from src.presentation.schemas.user import UserOut

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProductOut])
def list_products(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    # current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        products = list_products_composer(session)
        if products:
            return products
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def get_product(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        product = get_product_composer(session, id)
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(
    product: ProductCreate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        product = create_product_composer(
            session,
            product,
            created_by_id=current_user.id,
            company_id=current_company.id,
        )
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Product already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def update_product(
    id: int,
    product: ProductUpdate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    product = product.model_dump(exclude_unset=True)
    if current_user:
        product = update_product_composer(session, id, product)
        if product:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        product = delete_product_composer(session, id)
    if product:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.get(
    "/{id}/images/",
    status_code=status.HTTP_200_OK,
    response_model=list[ProductImageOut],
    tags=["images"],
)
async def list_product_images(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_company:
        product_images = list_product_images_composer(session, id)
        return product_images
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Product images not found."
    )


@router.post(
    "/{id}/images/",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductImageOut,
    tags=["images"],
)
async def add_product_image(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    images: list[UploadFile] = File(...),
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    for image in images:
        image_data = await image.read()

        unique_filename = str(uuid.uuid4())
        image_path = f"static/{unique_filename}{image.filename}"
        with open(image_path, "wb") as img:
            img.write(image_data)

        product_image = create_product_image_composer(session, id, image=image_path)

    if product_image:
        return product_image
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
    )


@router.delete(
    "/{id}/images/{id_image}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["images"],
)
def remove_product_image(
    id: int,
    id_image: int,
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    product_image = delete_product_image_composer(session, id, id_image)

    if product_image:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Image not found."
    )
