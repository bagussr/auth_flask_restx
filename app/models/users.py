from . import db, BaseModel


class Users(db.Model, BaseModel):
    """
    Users model
    """

    __tablename__ = "users"

    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Users {self.email}>"
