import factory
from factory import Faker
from sqlalchemy import orm

from src.infrastructure.database.models.address import Address
from src.infrastructure.database.models.card import Card
from src.infrastructure.database.models.company import Company
from src.infrastructure.database.models.user import User

Session = orm.scoped_session(orm.sessionmaker())


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session

    name = Faker("name")
    email = Faker("email")
    password = Faker("password")
    phone = Faker("phone_number")
    cpf = Faker("numerify")
    is_active = Faker("boolean")


class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        sqlalchemy_session = Session

    name = Faker("name")
    cnpj = Faker("numerify")
    website = Faker("url")
    owner = factory.SubFactory(UserFactory)
    is_approved = Faker("boolean")
    is_active = Faker("boolean")


class AddressFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Address
        sqlalchemy_session = Session

    name = Faker("name")
    postal_code = Faker("postcode")
    uf = Faker("state_abbr")
    city = Faker("city")
    neighborhood = Faker("city_suffix")
    street = Faker("street_name")
    number = Faker("building_number")
    complement = Faker("secondary_address")


class CardFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Card
        sqlalchemy_session = Session

    name = Faker("name")
    card_number = Faker("credit_card_number")
    expiration_month = Faker("month")
    expiration_year = Faker("year")
    cvc = Faker("credit_card_security_code")
