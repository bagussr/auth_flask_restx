from app import db
from sqlalchemy.ext.declarative import as_declarative, declared_attr
import uuid
from datetime import datetime


@as_declarative()
class BaseModel:
    """
    base model extended by another model
    """

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))
    created_date = db.Column(db.DateTime, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_uuid(cls, uuid_str):
        return cls.query.filter_by(uuid=uuid.UUID(uuid_str)).first()
