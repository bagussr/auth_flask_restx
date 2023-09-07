import jwt
import datetime

from app import db
from app.models.users import Users


class UserController:
    def get_all_users(self):
        return Users.query.all()

    def get_user_by_id(self, id):
        return Users.query.get(id)

    def get_user_by_username(self, username):
        return Users.query.filter_by(username=username).first()

    def create_user(self, name, username, password):
        user = Users(name=name, username=username, password_hash=password)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, id, username, password):
        user = Users.query.get(id)
        user.username = username
        user.password = password
        db.session.commit()
        return user

    def delete_user(self, id):
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user

    @classmethod
    def create_token(cls, user, secret_key, time=None):
        if time is None:
            time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token = jwt.encode({"id": user.id, "exp": time}, secret_key, algorithm="HS256")
        return token
