from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    created_date = fields.DateTime()
    updated_date = fields.DateTime()

    class Meta:
        fields = ("id", "username", "password", "created_date", "updated_date")
