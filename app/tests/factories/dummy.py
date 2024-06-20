import factory

from app.repository.db.models.dummy import DummyModel
from app.tests.factories.session import get_session


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = DummyModel
        sqlalchemy_session = get_session()
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
